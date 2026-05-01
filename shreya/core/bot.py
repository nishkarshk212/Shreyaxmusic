# Copyright (c) 2025 ShreyamousX1025
# Licensed under the MIT License.
# This file is part of ShreyaMusic


import pyrogram

from shreya import config, logger


class Bot(pyrogram.Client):
    def __init__(self):
        super().__init__(
            name="shreya",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            parse_mode=pyrogram.enums.ParseMode.HTML,
            max_concurrent_transmissions=7,
            link_preview_options=pyrogram.types.LinkPreviewOptions(is_disabled=True),
        )
        self.owner = config.OWNER_ID
        self.logger = config.LOGGER_ID
        self.bl_users = pyrogram.filters.user([])
        self.sudoers = pyrogram.filters.user([self.owner])

    async def boot(self):
        """
        Starts the bot and performs initial setup.

        Raises:
            SystemExit: If the bot fails to access the log group or is not an administrator in the logger group.
        """
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name
        self.username = self.me.username
        self.mention = self.me.mention
        logger.info(f"DEBUG: FULL ME: {self.me}")

        try:
            await self.send_message(self.logger, "Bot Started")
            get = await self.get_chat_member(self.logger, self.id)
            if get.status != pyrogram.enums.ChatMemberStatus.ADMINISTRATOR:
                logger.warning("Please promote the bot as an admin in logger group.")
        except Exception as ex:
            logger.warning(f"Bot has failed to access the log group: {self.logger}\nReason: {ex}")
        logger.info(f"Bot started as @{self.username}")

    @pyrogram.Client.on_message()
    async def log_messages(self, client, message):
        logger.info(f"RECEIVED MESSAGE: {message.text} from {message.from_user.id if message.from_user else 'None'} in {message.chat.id}")

    async def exit(self):
        """
        Asynchronously stops the bot.
        """
        await super().stop()
        logger.info("Bot stopped.")
