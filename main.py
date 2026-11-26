
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

WELCOME_CHANNEL_ID = 0  # Kanal ID buraya

@bot.event
async def on_ready():
    print(f"Bot aktif: {bot.user}")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)

    if channel:
        embed = discord.Embed(
            title="🎉 Hoş Geldin!",
            description=f"{member.mention}, sunucumuza hoş geldin!",
            color=discord.Color.green()
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=f"Üye sayısı: {member.guild.member_count}")

        await channel.send(embed=embed)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)

    if channel:
        embed = discord.Embed(
            title="👋 Görüşürüz!",
            description=f"**{member.name}** sunucumuzdan ayrıldı.",
            color=discord.Color.red()
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=f"Üye sayısı: {member.guild.member_count}")

        await channel.send(embed=embed)

bot.run("MTU3NTQ4Njc0ODU4MDkxMzIwMw.GiJ-CM.2ZkQiGicOKo5c2d4QuiWIABDtHbKoaycgyNzCA")
