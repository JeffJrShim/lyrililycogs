from redbot.core import commands 
import discord

class LyriLilyCogs(commands.Cog):
    """Lyrical Lily Utility Cogs"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def miyu(self, ctx):
        """Rule commands basically"""

    @miyu.group(invoke_without_command="True")
    async def rule0(self, ctx):
        """Rule 0 of MIYU'S HEAVENLY FANCLUB"""
        embed=discord.Embed(title="0. Abide to the Discord Terms of Service and Community Guidelines", description="Click on the links below to learn more about the terms of Service and Community Guidelines.\n[Terms](https://discord.com/terms)\n [Guidelines](https://discord.com/guidelines)",color=0xffcef2)
        embed.set_author(name="MIYU'S HEAVENLY FANCLUB Rules and Regulations")
        await ctx.send(embed=embed)

    @miyu.group(invoke_without_command="True")
    async def rule1(self,ctx):
        """Rule 1 of MIYU'S HEAVENLY FANCLUB"""
        embed=discord.Embed(title="1. Be respectful to other users and moderators.", description="Don't induce any arguments or anything that can hurt another user like racism and cyber-bullying.",color=0xffcef2)
        embed.set_author(name="MIYU'S HEAVENLY FANCLUB Rules and Regulations")
        await ctx.send(embed=embed)
    
    @miyu.group(invoke_without_command="True")
    async def rule2(self,ctx):
        """Rule 2 of MIYU'S HEAVENLY FANCLUB"""
        embed=discord.Embed(title="2. No swearing!", description="This is a server to talk nicely, so we are encouraging everyone to not swear, as well as bypassing swear words by using spoilers.",color=0xffcef2)
        embed.set_author(name="MIYU'S HEAVENLY FANCLUB Rules and Regulations")
        await ctx.send(embed=embed)

    @miyu.group(invoke_without_command="True")
    async def rule3(self,ctx):
        """Rule 3 of MIYU'S HEAVENLY FANCLUB"""
        embed=discord.Embed(title="3. No spamming!", description="You can spam in <#827203102998265927>, but not in other chatting channels. This is to not clog up the chat.",color=0xffcef2)
        embed.set_author(name="MIYU'S HEAVENLY FANCLUB Rules and Regulations")
        await ctx.send(embed=embed)
    
    @miyu.group(invoke_without_command="True")
    async def rule4(self,ctx):
        """Rule 4 of MIYU'S HEAVENLY FANCLUB"""
        embed=discord.Embed(title="4. Strictly No NSFW!", description="As the rule said, no NSFW content even on memes Also we've been seeing some NSFW art everywhere, including those in pixiv and especially the Rule 34 site. Anything that is NSFW will be given an instant mute, and it's an nude Miyu art, an instant 2-week ban. \n\n *Note: This rule bypasses the punishment counter (Run `{}miyu punishment`), as this rule gives you an instant ban once violated.*".format(ctx.prefix),color=0xffcef2)
        embed.set_author(name="MIYU'S HEAVENLY FANCLUB Rules and Regulations")
        await ctx.send(embed=embed)
    
    @miyu.group(invoke_without_command="True")
    async def rule5(self,ctx):
        """Rule 5 of MIYU'S HEAVENLY FANCLUB"""
        embed=discord.Embed(title="5. Keep anime and game spoilers in the right channel.", description="Be mindful for those that just got into the franchise and is starting to watch the anime (D4DJ: First Mix/D4DJ: Petit Mix) or reading the game stories in Groovy Mix. Put potential spoilers as a spoiler tag `||like this||` and keep them in <#817421163738300497>.",color=0xffcef2)
        embed.set_author(name="MIYU'S HEAVENLY FANCLUB Rules and Regulations")
        await ctx.send(embed=embed)
    
    @miyu.group(invoke_without_command="True")
    async def rule6(self,ctx):
        """Rule 6 of MIYU'S HEAVENLY FANCLUB"""
        embed=discord.Embed(title="6. Rules regarding to memes.", description="Rule 4 states that there shouldn't be NSFW content in the server, and that includes memes. We don't really mind if you sent them in other channels but it should be put on <#817421682384961556>.",color=0xffcef2)
        embed.set_author(name="MIYU'S HEAVENLY FANCLUB Rules and Regulations")
        await ctx.send(embed=embed)

    @miyu.group(invoke_without_command="True")
    async def rule7(self,ctx):
        """Rule 7 of MIYU'S HEAVENLY FANCLUB"""
        embed=discord.Embed(title="7. No advertising of any kind.", description="Unless approved by the moderators, you should not advertise. If you want to, kindly DM us first, and send the link of the one you want to advertise for verification (if it's an invite, we'll still need to double-check).",color=0xffcef2)
        embed.set_author(name="MIYU'S HEAVENLY FANCLUB Rules and Regulations")
        await ctx.send(embed=embed)
   
    @miyu.group(invoke_without_command="True")
    async def rule8(self,ctx):
        """Rule 8 of MIYU'S HEAVENLY FANCLUB"""
        embed=discord.Embed(title="8. Upload appropriate links and domains here.", description="We won't accept links that are suspicious, or even worse, those that grab your IP address. We also want users to be safe. \n The only domains that are accepted are 'youtube.com', 'facebook.com', 'twitter.com', 'discord.com', and the like.",color=0xffcef2)
        embed.set_author(name="MIYU'S HEAVENLY FANCLUB Rules and Regulations")
        await ctx.send(embed=embed)
    
    @miyu.group(invoke_without_command="True")
    async def rule9(self,ctx):
        """Rule 9 of MIYU'S HEAVENLY FANCLUB"""
        embed=discord.Embed(title="9. Check the pins.", description="Some extra info for each channel are put there. Those can be really important so check them every so often.",color=0xffcef2)
        embed.set_author(name="MIYU'S HEAVENLY FANCLUB Rules and Regulations")
        await ctx.send(embed=embed)
    
    @miyu.group(invoke_without_command="True")
    async def rule10(self,ctx):
        """Rule 10 of MIYU'S HEAVENLY FANCLUB"""
        embed=discord.Embed(title="10. We love Miyu here, so always protect her!", description="Do all your best to protect Miyu at all times. Protect her, as well as her innocence, purity, and cuteness! No lewd stuff of her! Please, it's literally on Rule 4!",color=0xffcef2)
        embed.set_author(name="MIYU'S HEAVENLY FANCLUB Rules and Regulations")
        await ctx.send(embed=embed)
        
    @miyu.group(invoke_without_command="True")
    async def rule11(self,ctx):
        """Rule 11 of MIYU'S HEAVENLY FANCLUB"""
        embed=discord.Embed(title="11. No hate speech on any character!", description="Yes, we love Miyu here, but how can we forget other characters from the franchise? Of course, you also need to protect and love them just like what we do to Miyu!",color=0xffcef2)
        embed.set_author(name="MIYU'S HEAVENLY FANCLUB Rules and Regulations")
        await ctx.send(embed=embed)
        
    @miyu.group(invoke_without_command="True")
    async def rule12(self,ctx):
        """Rule 12 of MIYU'S HEAVENLY FANCLUB"""
        embed=discord.Embed(title="12. Always remember to use your common sense.", description="It doesn't mean that something isn't listed down here you can do it. Remember, these are rule but you also need to treat them as guidelines! This is to make the fanclub peaceful and friendly. <:MiyuBliss:872056834821861386>",color=0xffcef2)
        embed.set_author(name="MIYU'S HEAVENLY FANCLUB Rules and Regulations")
        await ctx.send(embed=embed)
