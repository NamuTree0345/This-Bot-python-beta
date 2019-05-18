import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("/티스봇 도와줘 를 쳐봐!")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("/티스봇 안녕"):
        await message.channel.send("그래 안녕")
    if message.content.startswith("/티스봇 뭐해"):
        await message.channel.send("하이픽셀해")
    if message.content.startswith("/티스봇 심심해"):
        await message.channel.send("가서 게임해!!!!!!!!!!!")
    if message.content.startswith("/티스봇 채팅청소"):
        await message.channel.send("아직 출시되지 않은 기능입니다.")
    if message.content.startswith("/티스봇 뒤져"):
        await message.channel.send("니가 날 뒤질 수 있다고 생각해?")
    if message.content.startswith("/티스봇 니얼굴"):
        await message.channel.send("니얼굴이 더 못생김 ㅈㅅ")
    if message.content.startswith("/티스봇 정보"):
        await message.channel.send("```안녕! 난 너희들의 재미를 살리는 티스봇이야!\n너네들이 디스코드에서 심심하다면 날 언제나 불러!\n!참고! 봇이 오프라인일 때도 있습니다.\n버전: 0.3\n버전유형: BETA\n티스봇을 이용해 주셔서 감사합니다!```")
    if message.content.startswith("/티스봇 제작자"):
        await message.channel.send("제작자: redwikitv#0345, 특별기획: 설빙님")
    if message.content.startswith("/티스봇 니가뭔데"):
        await message.channel.send("~~나는 사람이면서 유튜버야~~ 가 아니라 나는 봇이야.")
    if message.content.startswith("/티스봇 도와줘"):
        await message.channel.send("```/티스봇 안녕\n/티스봇 뭐해\n/티스봇 심심해\n/티스봇 채팅청소\n/티스봇 뒤져\n/티스봇 니얼굴\n/티스봇 정보\n/티스봇 제작자\n/티스봇 니가뭔데```")

    #/ 채팅봇
    #안녕 / 채팅봇
    #도움말 / 채팅봇
    #제작자 / 채팅봇 ? / 채팅봇
    #채팅청소 / 채팅봇
    #니얼굴 / 채팅봇
    #뒤져 / 채팅봇
    #니얼굴못생김 / 채팅봇
    #니가뭔데

client.run("NTc5MTUxMzAzODEzNjI3OTQw.XN_bOg.yOb7kWueJSbeJ-8wBc3nfwy-kx0")