from telethon.utils import pack_bot_file_id

from userbot import jmthon
from userbot.core.logger import logging

from ..core.managers import edit_delete, edit_or_reply

LOGS = logging.getLogger(__name__)


@jmthon.ar_cmd(pattern="الايدي(?:\s|$)([\s\S]*)")
async def _(roze):
    input_str = roze.pattern_match.group(2)
    if input_str:
        try:
            p = await roze.client.get_entity(input_str)
        except Exception as e:
            return await edit_delete(roze, f"`{e}`", 5)
        try:
            if p.first_name:
                return await edit_or_reply(
                    roze, f" 𝖔𝖜𝖓 𝖎𝖉  `{input_str}` 𝖎𝖘\n⪼ `{p.id}`"
                )
        except Exception:
            try:
                if p.title:
                    return await edit_or_reply(
                        roze, f" 𝖔𝖜𝖓 𝖎𝖉 =  `{p.title}` 𝖎𝖘\n⪼ `{p.id}`"
                    )
            except Exception as e:
                LOGS.info(str(e))
        await edit_or_reply(roze, "** 𝖄𝖔𝖚 𝖒𝖚𝖘𝖙 𝖕𝖚𝖙 𝖙𝖍𝖊 𝖚𝖘𝖊𝖗 𝕴𝕯 𝖔𝖗 𝖗𝖊𝖕𝖑𝖞 𝖙𝖔 𝖙𝖍𝖊 𝖚𝖘𝖊𝖗 **")
    elif roze.reply_to_msg_id:
        r_msg = await roze.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await edit_or_reply(
                roze,
                f"**⪼: 𝕮𝖚𝖗𝖗𝖊𝖓𝖙 𝖈𝖍𝖆𝖙 𝕴𝕯 : **`{roze.chat_id}`\n**⪼ 𝖚𝖘𝖊𝖗 𝖎𝖉 : **`{r_msg.sender_id}`\n**⪼ ايدي الميديا: **`{bot_api_file_id}`",
            )

        else:
            await edit_or_reply(
                roze,
                f"** 𝖎𝖉 𝖈𝖚𝖗𝖗𝖊𝖓𝖙 𝖈𝖍𝖆𝖙 : **`{roze.chat_id}`\n**⪼ 𝖚𝖘𝖊𝖗 𝖎𝖉 : **`{r_msg.sender_id}`",
            )

    else:
        await edit_or_reply(roze, f"** 𝖎𝖉 𝖈𝖚𝖗𝖗𝖊𝖓𝖙 𝖈𝖍𝖆𝖙 : **`{roze.chat_id}`")
