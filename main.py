import discord
from discord.ext import commands

import time
import random
from PIL import Image
from io import BytesIO


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os

bot = commands.Bot(command_prefix="&")

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

@bot.event
async def on_ready():
    print('AMC HAS LOGGED INTO THE MATRIX')
    await bot.change_presence(activity = discord.Game(name = "&Help"))


@bot.command()
async def hello(ctx):
    await ctx.channel.send(random.choice([f'Sup! {ctx.author.mention}',f'Hello! {ctx.author.mention}',f'Hola {ctx.author.mention}',f'Go Away! {ctx.author.mention}',f'Good Day to you {ctx.author.mention}!',f'Get the hello out of here! {ctx.author.mention}']))


@bot.command()
async def randoProbo(ctx):
    def check(m):
        return m.author == ctx.author
    y2 = random.randrange(2002, 2021, 1)
    c2 = random.choice(['AMC_8', 'AMC_10A', 'AMC_10B', 'AMC_12A', 'AMC_12B'])
    p2 = random.randrange(1, 25, 1)
    print(str(y2) + " " + c2 + " " + str(p2))
    await ctx.reply(file=discord.File(getProblem(y2, c2, p2)))
    ans = getAnswer(y2, c2, p2)
    print(ans)
    msg = await bot.wait_for('message', check = check)
    if (msg.content == ans):
        await ctx.send(f'Congratulations {ctx.author.mention} you got it right!')
    else:
        await ctx.send(f'Uh Oh! {ctx.author.mention} you did an oopsie, better luck next time ')

@bot.command()
async def AMC10A(ctx):
    def check(m):
        return m.author == ctx.author
    y2 = random.randrange(2002, 2021, 1)
    c2 = 'AMC_10A'
    p2 = random.randrange(1, 25, 1)
    print(str(y2) + " " + c2 + " " + str(p2))
    await ctx.reply(file=discord.File(getProblem(y2, c2, p2)))
    ans = getAnswer(y2, c2, p2)
    print(ans)
    msg = await bot.wait_for('message', check = check)
    if (msg.content == ans):
        await ctx.send(f'Congratulations {ctx.author.mention} you got it right!')
    else:
        await ctx.send(f'Uh Oh! {ctx.author.mention} you did an oopsie, better luck next time ')

@bot.command()
async def AMC10B(ctx):
    def check(m):
        return m.author == ctx.author
    y2 = random.randrange(2002, 2021, 1)
    c2 = 'AMC_10B'
    p2 = random.randrange(1, 25, 1)
    print(str(y2) + " " + c2 + " " + str(p2))
    await ctx.reply(file=discord.File(getProblem(y2, c2, p2)))
    ans = getAnswer(y2, c2, p2)
    print(ans)
    msg = await bot.wait_for('message', check = check)
    if (msg.content == ans):
        await ctx.send(f'Congratulations {ctx.author.mention} you got it right!')
    else:
        await ctx.send(f'Uh Oh! {ctx.author.mention} you did an oopsie, better luck next time ')

@bot.command()
async def AMC12A(ctx):
    def check(m):
        return m.author == ctx.author
    y2 = random.randrange(2002, 2021, 1)
    c2 = 'AMC_12A'
    p2 = random.randrange(1, 25, 1)
    print(str(y2) + " " + c2 + " " + str(p2))
    await ctx.reply(file=discord.File(getProblem(y2, c2, p2)))
    ans = getAnswer(y2, c2, p2)
    print(ans)
    msg = await bot.wait_for('message', check = check)
    if (msg.content == ans):
        await ctx.send(f'Congratulations {ctx.author.mention} you got it right!')
    else:
        await ctx.send(f'Uh Oh! {ctx.author.mention} you did an oopsie, better luck next time ')

@bot.command()
async def AMC12B(ctx):
    def check(m):
        return m.author == ctx.author
    y2 = random.randrange(2002, 2021, 1)
    c2 = 'AMC_12B'
    p2 = random.randrange(1, 25, 1)
    print(str(y2) + " " + c2 + " " + str(p2))
    await ctx.reply(file=discord.File(getProblem(y2, c2, p2)))
    ans = getAnswer(y2, c2, p2)
    print(ans)
    msg = await bot.wait_for('message', check = check)
    if (msg.content == ans):
        await ctx.send(f'Congratulations {ctx.author.mention} you got it right!')
    else:
        await ctx.send(f'Uh Oh! {ctx.author.mention} you did an oopsie, better luck next time ')

@bot.command()
async def AMC8(ctx):
    def check(m):
        return m.author == ctx.author
    y2 = random.randrange(2000, 2021, 1)
    c2 = 'AMC_8'
    p2 = random.randrange(1, 25, 1)
    print(str(y2) + " " + c2 + " " + str(p2))
    await ctx.reply(file=discord.File(getProblem(y2, c2, p2)))
    ans = getAnswer(y2, c2, p2)
    print(ans)
    msg = await bot.wait_for('message', check = check)
    if (msg.content == ans):
        await ctx.send(f'Congratulations {ctx.author.mention} you got it right!')
    else:
        await ctx.send(f'Uh Oh! {ctx.author.mention} you did an oopsie, better luck next time ')

@bot.command()
async def specProb(ctx,arg1,arg2,arg3):
    def check(m):
        return m.author == ctx.author
    y2 = arg1
    c2 = ''
    if arg2 == 'AMC8':
        c2 = 'AMC_8'
    elif arg2 == 'AMC10A':
        c2 = 'AMC_10A'
    elif arg2 == 'AMC12A':
        c2 = 'AMC_12A'
    elif arg2 == 'AMC10A':
        c2 = 'AMC_10B'
    elif arg2 == 'AMC12B':
        c2 = 'AMC_12A'
    else:
        await ctx.reply("Incorrect Contest Input, smh get better")
        pass

    p2 = arg3
    await ctx.reply(file=discord.File(getProblem(y2, c2, p2)))
    ans = getAnswer(y2, c2, p2)
    print(ans)
    msg = await bot.wait_for('message', check = check)
    if (msg.content == ans):
        await ctx.send(f'Congratulations {ctx.author.mention} you got it right!')
    else:
        await ctx.send(f'Uh Oh! {ctx.author.mention} you did an oopsie, better luck next time ')

@bot.command()
async def Help(ctx):
    embed = discord.Embed(title="Commands",description="The Title is the Description",color=0x00ff00)
    embed.set_thumbnail(url = 'https://c.tenor.com/jUMex_rdqPwAAAAd/among-us-twerk.gif')
    embed.add_field(name="AMC",value="&randoProbo \n &AMC8 \n &AMC10A \n &AMC10B \n &AMC12A \n &AMC12B \n &specProb \"Year\" \"CompName\" \"Question Number\"" , inline=False)
    embed.add_field(name = "AIME",value = "Coming Soon", inline = False)
    await ctx.send(embed = embed)



def getProblem(y, c, q):
    year = str(y)
    CompName = c
    probNum = str(q)


    driver.get('https://artofproblemsolving.com/wiki/index.php/' + year + '_' + CompName + '_Problems/Problem_' + probNum)
    driver.fullscreen_window()
    try:
        driver.find_element(By.CLASS_NAME, "togglelink").click()
    except NoSuchElementException:
        pass
    time.sleep(2)
    problemPage = driver.get_screenshot_as_png()

    # Find Dimensions of Problem by exploiting formating of AOPS Site
    probWithNum = True
    solWithNum = True
    solWithoutNum = True

    try:
        driver.find_element(By.ID, 'Problem_' + probNum)
    except NoSuchElementException:
        probWithNum = False
    try:
        element2 = driver.find_element(By.ID, 'Solution_1')
    except NoSuchElementException:
        solWithNum = False
    try:
        driver.find_element(By.XPATH, "//*[contains(@id, 'Solution')]")
    except NoSuchElementException:
        solWithoutNum = False

    if probWithNum:
        element1 = driver.find_element(By.ID, 'Problem_' + probNum)
    else:
        element1 = driver.find_element(By.ID, 'Problem')

    location1 = element1.location

    if solWithNum:
        element2 = driver.find_element(By.XPATH,"//*[contains(@id, 'Solution')]")
        location2 = element2.location
    elif solWithoutNum:
        element2 = driver.find_element(By.XPATH, "//*[contains(@id, 'Solution')]")
        location2 = element2.location
    else:
        location2 = {'x': location1['x'], 'y': location1['y'] + 3500}

    # Creating Picture for Problem
    im = Image.open(BytesIO(problemPage))  # uses PIL library to open image in memory

    left = location1['x']
    top = location1['y']
    right = location2['x'] + 1800
    bottom = location2['y']

    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('screenshot.png')  # saves new cropped image

    screenshot = Image.open('screenshot.png')

    return 'screenshot.png'


def getAnswer(y, c, q):
    year = str(y)
    CompName = c
    probNum = str(q)


    # Getting Answer for Question (Could be Optimized in the sense that it gets all the answers from the test the problem is from)
    driver.get('https://artofproblemsolving.com/wiki/index.php/' + year + '_' + CompName + '_Answer_Key')
    element3 = driver.find_element(By.ID, 'mw-content-text').text
    answers = str(element3)
    answerList = answers.splitlines()

    return answerList[int(probNum) - 1]


t = open("token.txt")
token = t.read()
t.close()



bot.run(t)
