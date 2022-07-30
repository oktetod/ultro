# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

import re

from . import *

STRINGS = {
    1: """🎇 **Thanks for Deploying BayUserbot!**

• Here, are the Some Basic stuff from, where you can Know, about its Usage.""",
    2: """🎉** About BayUserbot**

🧿 Userbot is Pluggable and powerful Telethon Userbot, made in Python from Scratch. It is Aimed to Increase Security along with Addition of Other Useful Features.

❣ Made by **@baytoddd**""",
    3: """**💡• FAQs •**

-> [Username Tracker](https://t.me/ygabutkan)
-> [Keeping Custom Addons Repo](https://t.me/ygabutkan)
-> [Disabling Deploy message](https://t.me/ygabutkan)
-> [Setting up TimeZone](https://t.me/ygabutkan)
-> [About Inline PmPermit](https://t.me/ygabutkan)
-> [About Dual Mode](https://t.me/ygabutkan)
-> [Custom Thumbnail](https://t.me/ygabutkan)
-> [About FullSudo](https://t.me/ygabutkan)
-> [Setting Up PmBot](https://t.me/ygabutkan)
-> [Also Check](https://t.me/ygabutkan)

**• To Know About Updates**
  - Join @ygabutkan.""",
    4: f"""• `To Know All Available Commands`

  - `{HNDLR}help`
  - `{HNDLR}cmds`""",
    5: """• **For Any Other Query or Suggestion**
  - Move to **@ygabutkan**.

• Thanks for Reaching till END.""",
}


@callback(re.compile("initft_(\\d+)"))
async def init_depl(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 5:
        return await e.edit(
            STRINGS[5],
            buttons=Button.inline("<< Back", "initbk_" + str(4)),
            link_preview=False,
        )
    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", "initbk_" + str(CURRENT - 1)),
            Button.inline(">>", "initft_" + str(CURRENT + 1)),
        ],
        link_preview=False,
    )


@callback(re.compile("initbk_(\\d+)"))
async def ineiq(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 1:
        return await e.edit(
            STRINGS[1],
            buttons=Button.inline("Start Back >>", "initft_" + str(2)),
            link_preview=False,
        )
    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", "initbk_" + str(CURRENT - 1)),
            Button.inline(">>", "initft_" + str(CURRENT + 1)),
        ],
        link_preview=False,
    )
