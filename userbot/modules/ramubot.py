from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.ghosting(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu itu jelek`")
    sleep(2)
    await typew.edit("`Kedua kamu ya tetep jelek`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah pantesan kamu suka di ghosting`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Permisi,ku pantau kau anjing..**")


@register(outgoing=True, pattern='^.geez(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Vicky Peler☑️**")
    await typew.edit("**Vicky Peler✅**")
    sleep(1)
    await typew.edit("**Toni Gilaa☑️**")
    await typew.edit("**Toni Gilaa✅**")
    sleep(2)
    await typew.edit("**Karina Depresi☑️**")
    await typew.edit("**Karina Depresi✅**")
    sleep(2)
    await typew.edit("**Yunus Gajelas☑️**")
    await typew.edit("**Yunus Gajelas✅**")
    sleep(2)
    await typew.edit("**Adel GJM!☑️**")
    await typew.edit("**Adel GJM!✅**")
    sleep(2)
    await typew.edit("**Jia GJB!☑️**")
    await typew.edit("**Jia GJB!✅**")
    sleep(2)
    await typew.edit("**Imeh,MengRibet☑️**")
    await typew.edit("**Imeh,MengRibet✅**")
    sleep(2)
    await typew.edit("**Jeje,Mengintil☑️**")
    await typew.edit("**Jeje,Mengintil✅**")
    sleep(3)
    await typew.edit("**CUMA RAMA YANG BENER!**")


@register(outgoing=True, pattern='^.hapis(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Hapis,itu ganteng?`")
    sleep(1)
    await typew.edit("`orangnya setia?`")
    sleep(1)
    await typew.edit("`terus orangnya baik`")
    sleep(1)
    await typew.edit("`jadi gw jan disia siain ya anjing,gw limitid edition!`")


@register(outgoing=True, pattern='^.wah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wahh, GC nya tante wina keren`")
    sleep(2)
    await typew.edit("`Tapi, Yang gua liat, kok banyak badut`")
    sleep(2)
    await typew.edit("`Oh iya, Kan member+admin emng badut 🤡`")
    sleep(2)
    await typew.edit("`canda badut`")
    sleep(2)
    await typew.edit("`kasian jadi badutnya si wina.`")
    sleep(2)
    await typew.edit("`Kasian badut🤡, mending jadi badut gw aja, Wkwkwk`")
    sleep(3)
    await typew.edit("`Dah sini sama gw,gw bakal jadiin selayaknya ratu bukan badut`")

CMD_HELP.update({
    "rambot":
    "`.rambot`\
    \nUsage: menampilkan alive bot.\
    \n\n`.sadboy`\
    \nUsage: hiks\
    \n\n`.punten` ; `.geez`\
    \nUsage: misi."
})
