import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

channel_id = os.getenv("WELCOME_CHANNEL_ID", "1575479299891536104").strip()
WELCOME_CHANNEL_ID = int(channel_id)

@bot.event
async def on_ready():
    print(f"Bot aktif: {bot.user}")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)

    if channel:
        embed = discord.Embed(
            title="🎉 Welcome!",
            description=f"{member.mention}, Welcome channel!",
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
            title="👋 Goodbye!",
            description=f"**{member.name}** has exit channel.",
            color=discord.Color.red()
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.set_footer(text=f"Üye sayısı: {member.guild.member_count}")

        await channel.send(embed=embed)

bot.run(os.getenv("DISCORD_TOKEN"))
