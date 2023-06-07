import discord
from random import randint as ri
from discord.ext import commands
from discord.ui import Button, View

score = 0
checktime = 0
tries = 6


class wordlistner:
    def __init__(self, msg):
        self.msg = msg

    def update(self, msg):
        self.msg = msg

    def getMsg(self, msg):
        return msg


class vueInit(View):
    res = -1

    @discord.ui.button(label="nyes", style=discord.ButtonStyle.green)
    async def yes(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.res = 1
        await interaction.response.send_message("________________________________")
        self.stop()

    @discord.ui.button(label="nein", style=discord.ButtonStyle.red)
    async def no(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.res = 0
        await interaction.response.send_message("________________________________")
        global lost
        lost = False
        self.stop()

    async def disableAll(self):
        for child in self.children:
            child.disabled = True


def runBot():
    TOKEN = 'MTEwMDUyNjYyMTczNzM2MTQ3MA.GN1cj_.FKfZ9He2Utguvx7hcpCtoAMGj8x6HogO8aDJik'
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(intents=intents, command_prefix='!')
    messageManager = wordlistner("debut")

    @bot.command(aliases=["bj", "zwawin"])
    async def blackjack(ctx):
        global checktime, score
        score = 0
        checktime = 0
        gameRunning = True
        vue = vueInit()
        await ctx.send("aslema bik fi my game bitch")
        await ctx.send("t7eb tel3ab")
        await ctx.send(view=vue)
        carte = ri(1, 10)
        if not await vue.wait():
            if (vue.res == 1):
                checktime == 1
                await ctx.send("hethi lo3ba mta3 zhar kol wehed yejbed karta w eli yfout  lel 21 akthar wehed men 8ir \n mayfoutha yerba7 awel carta heya \n \n")
                await ctx.send(f"awel carta bdit biha heya {carte} => scorek = {carte}")
                score = carte
            else:
                await ctx.send("ok nvm ")
                gameRunning = False
                lost = False
        await vue.disableAll()
        lost = True
        while (gameRunning and score < 21):
            await ctx.send("tejbed karta")
            vue = vueInit()
            await ctx.send(view=vue)
            if not await vue.wait():
                if (vue.res == 1):
                    score += ri(1, 10)
                    await ctx.send(score)
                else:
                    gameRunning = False
                    score += ri(1, 10)
                    await ctx.send("hana bech nzido karta ken matfoutech el 21 ta5sar")
                    await ctx.send(score)
                    if (score > 21):
                        await ctx.send("fles is sad \n *you win*")
                        lost = False
                    else:
                        await ctx.send("fles is happy \n *you lost*")
                        lost = False

            await vue.disableAll()
        if (lost):
            await ctx.send("fles is happy \n *you lost*")

    @bot.command(aliases=["wordgame"])
    async def wordly(ctx):
        await ctx.send("hello in my wordle ")
        f = open("botwords.txt", "r")
        ch = f.read()
        ch = ch.replace("\n", "")
        words = ch.split(" ")
        word = words[ri(0, len(words))]
        word = word.upper()
        await ctx.send(f"your word is {word}")

        @bot.event
        async def on_message(msg):
            myword = msg.content.upper()
            if (not msg.author.bot) and len(str(myword).strip()) == 5:
                global tries
                resp = ""
                if (tries > 0):
                    tries -= 1
                    if myword == word:
                        await msg.channel.send("**"+myword+"**")
                        await msg.channel.send("you got it ya bro ")
                        myword = ""
                    else:
                        for i in range(len(myword)):
                            if myword[i] == word[i]:
                                resp += "**"+myword[i]+"** "
                            elif myword[i] in word:
                                resp += "__"+myword[i]+"__ "
                            else:
                                resp += "~~"+myword[i]+"~~ "
                        if (tries == 0):
                            resp = f"you lost the word was {word}"
                            tries = 6
                        await msg.channel.send(resp)

    bot.run(TOKEN)


runBot()
