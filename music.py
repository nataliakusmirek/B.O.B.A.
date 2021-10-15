import discord
from discord.ext import commands
import youtube_dl

client = commands.Bot(command_prefix="-", intents = discord.Intents.all())

class music(commands.Cog):
    def __init__(self, client):
      self.client = client

    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("You aren't in a voice channel what are you doing :(")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
            await ctx.send('Hello, what are we playing?')
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def skip(self,ctx):
        await ctx.voice_client.skip()

    @commands.command()
    async def play(self,ctx, url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        vc = ctx.voice_client
        if ctx.author.voice is None:
            await ctx.send("You aren't in a voice channel what are you doing :(")
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
            vc.play(source)

    @commands.command()
    async def playlist(ctx, url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        vc = ctx.voice_client
        if ctx.author.voice is None:
            await ctx.send("You aren't in a voice channel what are you doing :(")
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
            vc.play(source)

    @commands.command()
    async def sans(self,ctx):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        url = 'https://www.youtube.com/watch?v=WibFGyDMmYA'
        vc = ctx.voice_client
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
            vc.play(source)
        await ctx.send('**stan sans**')
    
    @commands.command()
    async def nyah(self,ctx):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        url = 'https://www.youtube.com/watch?v=PLDyWLbuptQ'
        vc = ctx.voice_client
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
            vc.play(source)

    @commands.command()
    async def zuzia(self,ctx):
        await ctx.send('ZUZIA IS THE REASON HALF OF THE TESTING WORKED THANK YOU')

    @commands.command()
    async def stop(self,ctx):
        await ctx.voice_client.stop()

    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()

    @commands.command()
    async def resume(self,ctx):
        await ctx.voice_client.resume()

    @commands.command()
    async def loop(self,ctx):
        await ctx.voice_client.loop()

def setup(client):
  client.add_cog(music(client))