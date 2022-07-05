import discord
import random
from discord.ext import commands
#from keep_alive import keep_alive
import requests
import asyncio

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)


token = 'OTMyMTE2NDAyNTAzMDMyODQy.Gs9Owo.IzDm_ocZAG-vXBrk84pY3cdcCmQF48GIYbv7U0'


@client.event
async def on_ready():
    print("Anti Pau lista")


#Comando para desterrar
@client.command()
async def desterrar(ctx, user: discord.Member = None):
    server = client.get_guild(885749866612023306)
    noPower = [
        "Y quien eres tu para usar ese comando?",
        "Creo que te faltan permisos, no?", "No quiero", "Obligame"
    ]
    await ctx.message.delete()
    staff =server.get_role(931713252465975337)
    pau =server.get_role(928727871420239913)
    dev =server.get_role(928727871420239913)
    cm =server.get_role(942963905989337119)
    adm =server.get_role(886342192279461928)
    mod =server.get_role(928731792347918447)
    sinfo =server.get_role(932131818898079795)
    smudae =server.get_role(930241549646827552)
    if staff in ctx.author.roles:
        desterrado =server.get_role(928737933949829130)
        sdp =server.get_role(886349781742530631)
        staff_channel = client.get_channel(928692551316308029)
        main_channel = client.get_channel(886350196672434196)
        if user == None:
            await ctx.send("No tengo a quien desterrar")
            return
        if user == ctx.message.author:
            await ctx.send("Te vas a desterrar solo(a)?")
            return
        if (staff in user.roles) or (pau in user.roles) or (
                dev in user.roles) or (cm in user.roles) or (
                    adm in user.roles) or (mod in user.roles) or (
                        sinfo in user.roles) or (smudae in user.roles):
            await ctx.send(random.choice(noPower))
        else:
            await user.add_roles(desterrado)
            await user.remove_roles(sdp)
            await staff_channel.send('He desterrado a ' + user.mention +
                                     " a peticion de " + ctx.author.mention)
            await main_channel.send(user.mention + " ha sido desterrado.")

    else:
        await ctx.send(random.choice(noPower))


#Exonerar
@client.command()
async def exonerar(ctx, user: discord.Member):
    server = client.get_guild(885749866612023306)
    await ctx.message.delete()
    staff =server.get_role(931713252465975337)
    pau =server.get_role(928727871420239913)
    dev =server.get_role(928727871420239913)
    cm =server.get_role(942963905989337119)
    adm =server.get_role(886342192279461928)
    mod =server.get_role(928731792347918447)
    sinfo =server.get_role(932131818898079795)
    smudae =server.get_role(930241549646827552)
    if staff in ctx.author.roles:
        desterrado =server.get_role(928737933949829130)
        sdp =server.get_role(886349781742530631)
        staff_channel = client.get_channel(928692551316308029)
        exonera_channel = client.get_channel(928692323699785819)
        if user == None:
            await ctx.send("No tengo a quien exonerar")
            return
        if user == ctx.message.author:
            await ctx.send("Te vas a exonerar solo(a)?")
            return
        await user.remove_roles(desterrado)
        await user.add_roles(sdp)
        await staff_channel.send('He exonerado a ' + user.mention +
                                 " a peticion de " + ctx.author.mention)
        await exonera_channel.send(user.mention + " has sido exonerado.")

    else:
        noPower = [
            "Y quien eres tu para usar ese comando?",
            "Creo que te faltan permisos, no?", "No quiero", "Obligame"
        ]
        await ctx.send(random.choice(noPower))


@client.command()
async def banp(ctx, user: discord.Member = None, *, reason=None):
    server = client.get_guild(885749866612023306)
    noPower = [
        "Y quien eres tu para usar ese comando?",
        "Creo que te faltan permisos, no?", "No quiero", "Obligame"
    ]
    await ctx.message.delete()
    staff =server.get_role(931713252465975337)
    pau =server.get_role(928727871420239913)
    dev =server.get_role(928727871420239913)
    cm =server.get_role(942963905989337119)
    adm =server.get_role(886342192279461928)
    mod =server.get_role(928731792347918447)
    sinfo =server.get_role(932131818898079795)
    smudae =server.get_role(930241549646827552)
    if (staff in ctx.author.roles) or (pau in ctx.author.roles) or (dev in ctx.author.roles) or (cm in ctx.author.roles) or (adm in ctx.author.roles) or (mod in ctx.author.roles):
        staff_channel = client.get_channel(928692551316308029)
        if user == None:
            await ctx.send("No tengo a quien banear.")
            return
        if user == ctx.message.author:
            await ctx.send("No puedes banearte solo(a)")
            return
        if (staff in user.roles) or (pau in user.roles) or (
                dev in user.roles) or (cm in user.roles) or (
                    adm in user.roles) or (mod in user.roles) or (
                        sinfo in user.roles) or (smudae in user.roles):
            await ctx.send(random.choice(noPower))
        else:
            #Banear
            embed = discord.Embed(title="Baneo de " + user.name,
                                  color=14495300)
            embed.add_field(name="Nombre", value=user.mention, inline=False)
            embed.add_field(name="ID", value=user.id, inline=False)
            if (reason == None):
                txtReason = "Porque me aburri"
            else:
                txtReason = str(reason)

            embed.add_field(name="Razon", value=txtReason, inline=False)
            embed.add_field(name="Pedido por", value=ctx.author.mention)
            embed.set_thumbnail(url=user.avatar_url)
            await staff_channel.send(embed=embed)
            await user.ban(reason=txtReason)

    else:
        await ctx.send(random.choice(noPower))


#kick command
@client.command()
async def kickp(ctx, user: discord.Member = None, *, reason=None):
    server = client.get_guild(885749866612023306)
    noPower = [
        "Y quien eres tu para usar ese comando?",
        "Creo que te faltan permisos, no?", "No quiero", "Obligame"
    ]
    await ctx.message.delete()
    staff =server.get_role(931713252465975337)
    pau =server.get_role(928727871420239913)
    dev =server.get_role(928727871420239913)
    cm =server.get_role(942963905989337119)
    adm =server.get_role(886342192279461928)
    mod =server.get_role(928731792347918447)
    sinfo =server.get_role(932131818898079795)
    smudae =server.get_role(930241549646827552)
    if (staff in ctx.author.roles) or (pau in ctx.author.roles) or (dev in ctx.author.roles) or (cm in ctx.author.roles) or (adm in ctx.author.roles) or (mod in ctx.author.roles):
        staff_channel = client.get_channel(928692551316308029)
        if user == None:
            await ctx.send("No tengo a quien hacer kick.")
            return
        if user == ctx.message.author:
            await ctx.send("No puedes kickearte solo(a)")
            return
        if (staff in user.roles) or (pau in user.roles) or (
                dev in user.roles) or (cm in user.roles) or (
                    adm in user.roles) or (mod in user.roles) or (
                        sinfo in user.roles) or (smudae in user.roles):
            await ctx.send(random.choice(noPower))
        else:
            #Kick
            embed = discord.Embed(title="Kick de " + user.name, color=14495300)
            embed.add_field(name="Nombre", value=user.mention, inline=False)
            embed.add_field(name="ID", value=user.id, inline=False)
            if (reason == None):
                txtReason = "Porque me aburri"
            else:
                txtReason = str(reason)

            embed.add_field(name="Razon", value=txtReason, inline=False)
            embed.add_field(name="Pedido por", value=ctx.author.mention)
            embed.set_thumbnail(url=user.avatar_url)
            await staff_channel.send(embed=embed)
            await user.kick(reason=txtReason)

    else:
        await ctx.send(random.choice(noPower))


#Revisar cada mensaje
@client.event
async def on_message(message):
    xp_channel = [
        886350196672434196, 928688157191458876, 936176632446742579,
        919779324759011349, 928688234958041098, 929760249836101632,
        929760568611569694, 928688110252986408, 929761279277670431,
        929761544072474724, 929760905300967424, 931697976252964884,
        930223824891428955, 928689970036748348, 928689946724818974,
        930962248665554944, 928689152818569278, 928687756983566356,
        928689870967283742, 928689921789669396, 930141284700667975,
        928688949436755998
    ]
    test_channel = [928682972540977192]
    server = client.get_guild(885749866612023306)
    miembro_chikito = server.get_role(945914570957017088)
    novato = server.get_role(945916421370679306)
    aprendiz = server.get_role(945916832693493800)
    miembro_junior = server.get_role(945917489001398322)
    miembro_pro = server.get_role(945917779435986984)
    maestro = server.get_role(945918208488116264)
    inmortal = server.get_role(945918386947391498)
    if message.channel.id in xp_channel:
        URL = "https://mg-programs.com/checkUser.php"
        PARAMS = {'id': message.author.id}
        r = requests.get(url=URL, params=PARAMS)
        stats = r.json()
        if not message.author.bot:
            if stats['status'] == "void":
                #No existe, por ende se debe crear
                url_add = "https://mg-programs.com/addUser.php"
                params_add = {'id': message.author.id}
                add = requests.post(url=url_add, data=params_add)
                await message.author.add_roles(novato)
            else:
                level = int(stats['Level'])
                xp = int(stats['XP'])
                new_xp = xp + 1
                level_up = level + 1
                if new_xp < ((75 * (level_up**2) - (75 * level_up))):
                    url_update = "https://mg-programs.com/updateData.php"
                    params_update = {
                        'id': message.author.id,
                        'xp': new_xp,
                        'level': level
                    }
                    update = requests.post(url=url_update, data=params_update)
                elif new_xp >= ((75 * (level_up**2) - (75 * level_up))):
                    #
                    url_update = "https://mg-programs.com/updateData.php"
                    params_update = {
                        'id': message.author.id,
                        'xp': new_xp,
                        'level': level_up
                    }
                    update = requests.post(url=url_update, data=params_update)
                    test_channel = client.get_channel(928682972540977192)
                    levelup_channel = client.get_channel(928689843599446017)
                    if level_up == 3:
                        rankUp = "\n\nAscendiste a " + aprendiz.name
                    elif level_up == 8:
                        rankUp = "\n\nAscendiste a " + miembro_chikito.name
                    elif level_up == 16:
                        rankUp = "\n\nAscendiste a " + miembro_junior.name
                    elif level_up == 26:
                        rankUp = "\n\nAscendiste a " + miembro_pro.name
                    elif level_up == 36:
                        rankUp = "\n\nAscendiste a " + maestro.name
                    elif level_up == 51:
                        rankUp = "\n\nAscendiste a " + inmortal.name
                    else:
                        rankUp = ""
                    await levelup_channel.send(
                        " <a:6761zerotwoclapping:929602578638065715>Felicidades "
                        + message.author.mention +
                        "<a:6761zerotwoclapping:929602578638065715>\n\n S Ó T A N O D E P A U ツ ™\n\n"
                        +
                        "<a:9078zerotwohypedfast:932130638348312636> Subiste a nivel "
                        + str(level_up) +
                        "<a:9078zerotwohypedfast:932130638348312636>" +
                        rankUp +
                        "\n\nhttps://tenor.com/view/anime-pink-hair-zero-two-darling-in-the-franxx-002-gif-17763486"
                    )
                    #Check roles at level up
                    if level_up <= 2:
                        await message.author.add_roles(novato)
                    elif 3 <= level_up <= 7:
                        await message.author.remove_roles(novato)
                        await message.author.add_roles(aprendiz)
                    elif 8 <= level_up <= 15:
                        await message.author.remove_roles(novato)
                        await message.author.remove_roles(aprendiz)
                        await message.author.add_roles(miembro_chikito)
                    elif 16 <= level_up <= 25:
                        await message.author.remove_roles(novato)
                        await message.author.remove_roles(aprendiz)
                        await message.author.remove_roles(miembro_chikito)
                        await message.author.add_roles(miembro_junior)
                    elif 26 <= level_up <= 35:
                        await message.author.remove_roles(miembro_chikito)
                        await message.author.remove_roles(novato)
                        await message.author.remove_roles(aprendiz)
                        await message.author.remove_roles(miembro_junior)
                        await message.author.add_roles(miembro_pro)
                    elif 36 <= level_up <= 50:
                        await message.author.remove_roles(miembro_chikito)
                        await message.author.remove_roles(novato)
                        await message.author.remove_roles(aprendiz)
                        await message.author.remove_roles(miembro_junior)
                        await message.author.remove_roles(miembro_pro)
                        await message.author.add_roles(maestro)
                    elif level_up > 50:
                        await message.author.remove_roles(miembro_chikito)
                        await message.author.remove_roles(novato)
                        await message.author.remove_roles(aprendiz)
                        await message.author.remove_roles(miembro_junior)
                        await message.author.remove_roles(miembro_pro)
                        await message.author.remove_roles(maestro)
                        await message.author.add_roles(inmortal)

    foo = ["Ew", "Ay no", "Bye"]
    evil = [
        "No hay sistema", "No me menciones", "Que quieres?", "Quieres ban?",
        "Obligame", "Ahora no joven", "Andas como pregunton hoy, no?"
    ]
    mensajesP = ["Hola, tú", "A ti no te odio tanto", "Hola supp #2"]
    if message.author == client.user or message.author.id == 931315987888873534 or message.mention_everyone or message.channel.id == 928688157191458876:
        return

    msg = message.content.lower()
    if msg.startswith('holi') is True:
        if message.author.id == 597302123729911831:
            await message.reply(random.choice(mensajesP))
        else:
            await message.reply(message.author.mention + " " +
                                random.choice(foo))
    if msg.startswith('contexto') is True:
        await message.reply("TE LA COMES SIN PRETEXTO")
    if 'simp' in msg.split() or 'simpeo' in msg.split():
        await message.reply('Ewww un simp')
    if client.user.mentioned_in(message):
        await message.reply(random.choice(evil))
    if msg.startswith('ya vine') is True:
        await message.reply("Vete otra vez")
    #End
    await client.process_commands(message)


@client.command()
async def rango(ctx, user: discord.Member = None):
    if user == None:
        target = ctx.author
    else:
        target = user
    xp_channel = [
        886350196672434196, 928688157191458876, 936176632446742579,
        919779324759011349, 928688234958041098, 929760249836101632,
        929760568611569694, 928688110252986408, 929761279277670431,
        929761544072474724, 929760905300967424, 928682972540977192,
        930141284700667975, 928687329311338597
    ]
    test_channel = [928682972540977192]
    if ctx.channel.id in xp_channel:
        URL = "https://mg-programs.com/findRank.php"
        PARAMS = {'id': target.id}
        r = requests.get(url=URL, params=PARAMS)
        stats = r.json()
        if not ctx.author.bot:
            if stats['status'] == "void":
                #No existe, por ende se debe crear
                await ctx.channel.send(
                    "No has enviado ningun mensaje por lo que no estas en el ranking"
                )
            else:
                level = int(stats['Level'])
                xp = int(stats['XP'])
                rank = int(stats['Rank'])
                level_up=level+1
                next_xp = (75 * (level_up**2) - (75 * level_up))
                if level <= 2:
                    msgColor = 15132648
                    currentRank="Novato"
                    nextrank="Aprendiz"
                elif 3 <= level <= 7:
                    msgColor = 14495300
                    currentRank="Aprendiz"
                    nextrank="Miembro chikito"
                elif 8 <= level <= 15:
                    msgColor = 16027660
                    currentRank="Miembro chikito"
                    nextrank="Miembro junior"
                elif 16 <= level <= 25:
                    msgColor = 16632664
                    currentRank="Miembro junior"
                    nextrank="Miembro pro"
                elif 26 <= level <= 35:
                    msgColor = 7909721
                    currentRank="Miembro pro"
                    nextrank="Maestro"
                elif 36 <= level <= 50:
                    msgColor = 6139372
                    currentRank="Maestro"
                    nextrank="Inmortal"
                elif level > 50:
                    msgColor = 11177686
                    currentRank="Inmortal"
                    nextrank="???"

                embed = discord.Embed(title="Estadisticas de " + target.name +" en el servidor",color=msgColor)
                embed.add_field(name="☆₍ᐢ⑅ᐢ₎・Nombre",value=target.mention,inline=False)
                embed.add_field(name="☆₍ᐢ⑅ᐢ₎・Posicion en el servidor",value=str(rank) + "/" +str(ctx.guild.member_count),inline=False)
                embed.add_field(name="☆₍ᐢ⑅ᐢ₎・Rango actual",value=currentRank,inline=False)
                embed.add_field(name="☆₍ᐢ⑅ᐢ₎・Siguiente rango",value=nextrank,inline=False)
                embed.add_field(name="☆₍ᐢ⑅ᐢ₎・Experiencia", value=str(xp)+"/"+str(next_xp), inline=False)
                embed.add_field(name="☆₍ᐢ⑅ᐢ₎・PauCoin", value="0", inline=False)
                embed.set_thumbnail(url=target.avatar_url)
                await ctx.send(embed=embed)


#Mute command
@client.command()
async def mutep(ctx, user: discord.Member = None, *, mute_time=None):
    server = client.get_guild(885749866612023306)
    noPower = [
        "Y quien eres tu para usar ese comando?",
        "Creo que te faltan permisos, no?", "No quiero", "Obligame"
    ]
    await ctx.message.delete()
    staff =server.get_role(931713252465975337)
    pau =server.get_role(928727871420239913)
    dev =server.get_role(928727871420239913)
    cm =server.get_role(942963905989337119)
    adm =server.get_role(886342192279461928)
    mod =server.get_role(928731792347918447)
    sinfo =server.get_role(932131818898079795)
    smudae =server.get_role(930241549646827552)
    if mute_time == None:
        finalTime = 30
        go = True
    else:
        if mute_time.isnumeric():
            finalTime = int(mute_time)
            go = True
        else:
            go = False

    if (go is True):
        if (staff in ctx.author.roles) or (pau in ctx.author.roles) or (dev in ctx.author.roles) or (cm in ctx.author.roles) or (adm in ctx.author.roles) or (mod in ctx.author.roles):
            staff_channel = client.get_channel(928692551316308029)
            muted_role = server.get_role(933470492864688148)
            if user == None:
                await ctx.send("No tengo a quien hacer mute.")
                return
            if user == ctx.message.author:
                await ctx.send("Si quieres mutearte, solo deja de escribir(?)")
                return
            if (staff in user.roles) or (pau in user.roles) or (
                    dev in user.roles) or (cm in user.roles) or (
                        adm in user.roles) or (mod in user.roles) or (
                            sinfo in user.roles) or (smudae in user.roles):
                await ctx.send(random.choice(noPower))
            else:
                #Mute
                url_mute = "https://mg-programs.com/findMutes.php"
                param_mute = {'id': user.id}
                r = requests.get(url=url_mute, params=param_mute)
                stats = r.json()
                if not ctx.author.bot:
                    if stats['status'] == "void":
                        #No existe, por ende se debe crear
                        await staff_channel.send(
                            "Se ha generado un error al mutear a " +
                            user.mention)
                    else:
                        mutes = int(stats['Mutes'])
                        next_mute = mutes + 1
                        if (next_mute >= 3):
                            #Kick
                            embed = discord.Embed(title="Kick de " + user.name,
                                                  color=14495300)
                            embed.add_field(name="Nombre",
                                            value=user.mention,
                                            inline=False)
                            embed.add_field(name="ID",
                                            value=user.id,
                                            inline=False)
                            txtReason = "Mute #3"
                            embed.add_field(name="Razon",
                                            value=txtReason,
                                            inline=False)
                            embed.add_field(name="Pedido por", value="Yo uwu")
                            embed.set_thumbnail(url=user.avatar_url)
                            await staff_channel.send(embed=embed)
                            url_update = "https://mg-programs.com/clearMutes.php"
                            params_update = {'id': user.id}
                            update = requests.post(url=url_update,
                                                   data=params_update)
                            await user.kick(reason=txtReason)
                        else:
                            url_update = "https://mg-programs.com/addMute.php"
                            params_update = {'id': user.id, 'mutes': next_mute}
                            update = requests.post(url=url_update,
                                                   data=params_update)
                            await user.add_roles(muted_role)
                            await ctx.send("INTENTA HABLAR AHORA")

                            await staff_channel.send("He muteado a " +
                                                     user.mention +
                                                     " a peticion de " +
                                                     ctx.author.mention +
                                                     " por " + str(finalTime) +
                                                     " minutos")
                            await asyncio.sleep(finalTime * 60)
                            await user.remove_roles(muted_role)
                            await staff_channel.send(user.mention +
                                                     " ya puede hablar")

        else:
            await ctx.send(random.choice(noPower))

    else:
        await ctx.send(
            "Hubo un error en el tiempo, por favor revisa el comando.",
            delete_after=5)


#Warn command
@client.command()
async def warnp(ctx, user: discord.Member = None, *, reason=None):
    server = client.get_guild(885749866612023306)
    noPower = [
        "Y quien eres tu para usar ese comando?",
        "Creo que te faltan permisos, no?", "No quiero", "Obligame"
    ]
    await ctx.message.delete()
    staff =server.get_role(931713252465975337)
    pau =server.get_role(928727871420239913)
    dev =server.get_role(928727871420239913)
    cm =server.get_role(942963905989337119)
    adm =server.get_role(886342192279461928)
    mod =server.get_role(928731792347918447)
    sinfo =server.get_role(932131818898079795)
    smudae =server.get_role(930241549646827552)

    if (staff in ctx.author.roles) or (pau in ctx.author.roles) or (dev in ctx.author.roles) or (cm in ctx.author.roles) or (adm in ctx.author.roles) or (mod in ctx.author.roles):
        staff_channel = client.get_channel(928692551316308029)
        muted_role = server.get_role(933470492864688148)
        if user == None:
            await ctx.send("No tengo a quien hacer warn.")
            return
        if user == ctx.message.author:
            await ctx.send("Te haras warn solo(a)????")
            return
        if (staff in user.roles) or (pau in user.roles) or (
                dev in user.roles) or (cm in user.roles) or (
                    adm in user.roles) or (mod in user.roles) or (
                        sinfo in user.roles) or (smudae in user.roles):
            await ctx.send(random.choice(noPower))
        else:
            #Warn
            url_mute = "https://mg-programs.com/findWarns.php"
            param_mute = {'id': user.id}
            r = requests.get(url=url_mute, params=param_mute)
            stats = r.json()
            if not ctx.author.bot:
                if stats['status'] == "void":
                    #No existe, por ende se debe crear
                    await staff_channel.send(
                        "Se ha generado un error al hacer warn a " +
                        user.mention)
                else:
                    warns = int(stats['Warns'])
                    mutes = int(stats['Mutes'])
                    next_warn = warns + 1
                    next_mute = mutes + 1
                    if (next_warn >= 3):
                        if (next_mute >= 3):
                            #Kick
                            embed = discord.Embed(title="Kick de " + user.name,
                                                  color=14495300)
                            embed.add_field(name="Nombre",
                                            value=user.mention,
                                            inline=False)
                            embed.add_field(name="ID",
                                            value=user.id,
                                            inline=False)
                            txtReason = "Mute #3"
                            embed.add_field(name="Razon",
                                            value=txtReason,
                                            inline=False)
                            embed.add_field(name="Pedido por", value="Yo uwu")
                            embed.set_thumbnail(url=user.avatar_url)
                            await staff_channel.send(embed=embed)
                            url_update = "https://mg-programs.com/clearMutes.php"
                            params_update = {'id': user.id}
                            update = requests.post(url=url_update,
                                                   data=params_update)
                            await user.kick(reason=txtReason)
                        else:
                            url_update = "https://mg-programs.com/addMute.php"
                            params_update = {'id': user.id, 'mutes': next_mute}
                            update = requests.post(url=url_update,
                                                   data=params_update)
                            url_update2 = "https://mg-programs.com/clearWarns.php"
                            params_update2 = {'id': user.id}
                            update2 = requests.post(url=url_update2,
                                                    data=params_update2)
                            await user.add_roles(muted_role)
                            await ctx.send("INTENTA HABLAR AHORA")
                            await staff_channel.send(
                                "He muteado a " + user.mention +
                                " ya que ha acumulado 3 warns")
                            await asyncio.sleep(1800)
                            await user.remove_roles(muted_role)
                            await staff_channel.send(user.mention +
                                                     " ya puede hablar")
                    else:
                        url_warn = "https://mg-programs.com/addWarn.php"
                        params_warn = {'id': user.id, 'warns': next_warn}
                        warnReq = requests.post(url=url_warn, data=params_warn)
                    #Warn
                    embed = discord.Embed(title="Warn de " + user.name,
                                          color=14495300)
                    embed.add_field(name="Nombre",
                                    value=user.mention,
                                    inline=False)
                    embed.add_field(name="ID", value=user.id, inline=False)
                    if (reason == None):
                        txtReason = "Porque me aburri"
                    else:
                        txtReason = str(reason)
                    embed.add_field(name="Razon",
                                    value=txtReason,
                                    inline=False)
                    embed.add_field(name="Pedido por",
                                    value=ctx.author.mention)
                    embed.set_thumbnail(url=user.avatar_url)
                    await staff_channel.send(embed=embed)

    else:
        await ctx.send(random.choice(noPower))


#Top5 command
@client.command()
async def top5(ctx):
    server = client.get_guild(885749866612023306)
    URL = "https://mg-programs.com/top5.php"
    PARAMS = {'id': ""}
    r = requests.get(url=URL, params=PARAMS)
    stats = r.json()
    embed = discord.Embed(title="Top 5 Usuarios del servidor")
    i = 0
    while (i < 5):
        x = i + 1
        us_id = int(stats[i][0])
        user = await client.fetch_user(us_id)
        xp = stats[i][1]
        embed.add_field(name="Rank #" + str(x),
                        value=user.name + "(" + str(xp) + "XP)",
                        inline=False)
        i += 1

    await ctx.send(embed=embed)

#All mudae
@client.command()
async def allmudae(ctx):
    server = client.get_guild(885749866612023306)
    mudae = server.get_role(932083203907420170)
    await ctx.message.delete()
    await ctx.send(mudae.mention)

#Minecraft
@client.command()
async def tagMinecraft(ctx):
    server = client.get_guild(885749866612023306)
    mudae = server.get_role(932068242434949180)
    await ctx.message.delete()
    await ctx.send(mudae.mention)

    #Conoceme
@client.command()
async def conoceme(ctx):
    conoceme_channel = client.get_channel(928683101587144734)
    
    message = "Twitch: www.twitch.tv/paugamer31 \n\n Instagram: www.instagram.com/paugamer31\n\n Facebook: www.facebook.com/paugamer31"
    await ctx.message.delete()
    await conoceme_channel.send(message)
#Test
@client.command()
async def testIntro(ctx):
    await join_message_run(ctx.author)
    

#Test
async def join_message_run(user: discord.Member = None):
    server = client.get_guild(885749866612023306)
    verify_channel = client.get_channel(931721000746381343)
    rules_channel = client.get_channel(886343783816527972)
    roles_channel = client.get_channel(928687279185215518)
    welcome_message = "♡︰₊˚ Bienvenid@ al Sótano de Pau ˚₊︰♡\n\n" + "<a:m_:929603736261779456>Bienvenido al servidor " + user.mention +'. No olvides:\n<:3454pinkpixelhearts:931643955429396600>Ir al canal de '+ verify_channel.mention+' para acceder a todos los canales.\n<:3454pinkpixelhearts:931643955429396600>Leer las reglas en el canal de '+ rules_channel.mention+'.\n<:3454pinkpixelhearts:931643955429396600>Pasar por el canal de '+roles_channel.mention+' para desbloquear canales y personalizar tu perfil.\n<:3454pinkpixelhearts:931643955429396600>Si tienes alguna duda, habla con algún admin o mod.\n\n<a:m_:929603736261779456>Gracias a ti somos ' + str(server.member_count)+' miembros en el sótano.'
    welcome_channel = client.get_channel(886343738014699630)
    #await welcome_channel.send(embed=embed)
    await welcome_channel.send(welcome_message,file=discord.File('Intro.gif'))
    
#On member join   
@client.event
async def on_member_join(member):
    '''
    server = client.get_guild(885749866612023306)
    us_id = member.id
    user = client.get_user(us_id)
    embed = discord.Embed(title="♡︰₊˚ Bienvenid@ al Sótano de Pau ˚₊︰♡",description="<a:m_:929603736261779456>Bienvenido al servidor " + user.mention +'. No olvides:\n<:3454pinkpixelhearts:931643955429396600>Ir al canal de ["#Verificación"](https://discord.com/channels/885749866612023306/931721000746381343) para acceder a todos los canales.\n<:3454pinkpixelhearts:931643955429396600>Leer las reglas en el canal de [#Normativa](https://discord.com/channels/885749866612023306/886343783816527972/931612671508361319).\n<:3454pinkpixelhearts:931643955429396600>Pasar por el canal de ["#Roles"](https://discord.com/channels/885749866612023306/928687279185215518) para desbloquear canales y personalizar tu perfil.\n<:3454pinkpixelhearts:931643955429396600>Si tienes alguna duda, habla con algún admin o mod.\n\n<a:m_:929603736261779456>Gracias a ti somos ' + str(server.member_count)+' miembros en el sótano.')
    embed.set_image(url='https://i.pinimg.com/originals/fa/74/6d/fa746df97531d7b689a9d2a4ae1cf909.gif')
    embed.set_thumbnail(url=member.avatar_url)
    welcome_channel = client.get_channel(886343738014699630)
    await welcome_channel.send(embed=embed)
   '''
    await join_message_run(member)

#Run client
#keep_alive()
client.run(token)
