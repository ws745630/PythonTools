#!/Users/Jesli/opt/anaconda3/bin/python
# -*- coding: UTF-8 -*-

import io, os
import UnityPy
import sys, getopt
import traceback
import json
import UnityPy
class UnPackUnityAsset:
    def __init__(self, inFile, outDir):
        self.inFile = inFile
        self.outDir = outDir

    def GetOutDirByType(self, typeName):
        return os.path.join(self.outDir, typeName)

    def SaveTexture2D(self, data):
        targetDir = self.GetOutDirByType('Texture2D')
        isExist = os.path.exists(targetDir)

        if not isExist:
            os.makedirs(targetDir)

        if data.m_Width != 0:
            outPath = os.path.join(targetDir, data.name + ".png")
            try:
                data.image.save(outPath)
            except Exception as e:
                print(traceback.format_exc())
                pass
        else:
            print(data.name, "Can't be processed")

    def SaveSprite(self, data):
        targetDir = self.GetOutDirByType('Sprite')
        isExist = os.path.exists(targetDir)

        if not isExist:
            os.makedirs(targetDir)

        outPath = os.path.join(targetDir, data.name + ".png")
        try:
            data.image.save(outPath)
        except:
            pass

    def SaveMesh(self, mesh):
        targetDir = self.GetOutDirByType('Mesh')
        isExist = os.path.exists(targetDir)

        if not isExist:
            os.makedirs(targetDir)

        outPath = os.path.join(targetDir, mesh.name + ".obj")
        with open(outPath, "wt", newline = "") as f:
            exportData = mesh.export()
            if isinstance(exportData, str):
                f.write(mesh.export())
            else:
                print(mesh.name, 'is not a mesh')


    def SaveText(self, text):
        targetDir = self.GetOutDirByType('TextAsset')
        isExist = os.path.exists(targetDir)

        if not isExist:
            os.makedirs(targetDir)
        outPath = os.path.join(targetDir, text.name + ".txt")

        with open(outPath, "wb") as f:
            f.write(bytes(text.script))

    def SaveMono(self, mono):
        targetDir = self.GetOutDirByType('MonoBehaviour')
        isExist = os.path.exists(targetDir)

        if not isExist:
            os.makedirs(targetDir)
        outPath = os.path.join(targetDir, mono.name + ".txt")

        if mono.script:
            with open(outPath, "wt", encoding="utf8") as f:
                try:
                    print(type(mono.script))
                    f.write(json.dump(mono.script.read().to_dict(), f, ensure_ascii = False, indent=4))
                except Exception as e:
                    print(traceback.format_exc())
                    pass
        
    def SaveShader(self, shader):
        targetDir = self.GetOutDirByType('Shaders')
        isExist = os.path.exists(targetDir)

        if not isExist:
            os.makedirs(targetDir)
        showName = shader.m_ParsedForm.m_Name
        showName = showName.replace(' ', '_')
        showName = showName.replace('/', '_')
        print(shader.m_ParsedForm.m_Name, showName)
        outPath = os.path.join(targetDir, showName + ".txt")

        with open(outPath, "wt", encoding="utf8") as f:
            f.write(shader.export())


    def UnPack(self, *args):
        self.env = UnityPy.load(self.inFile)
        all = True if len(args) == 0 else False
        
        for obj in self.env.objects:
            if all or (obj.type in args):
                if obj.type.name == "Texture2D":
                    data = obj.read()
                    self.SaveTexture2D(data)
                elif obj.type.name == "Sprite":
                    data = obj.read()
                    self.SaveSprite(data)
                elif obj.type.name == "Mesh":
                    mesh = obj.read()
                    self.SaveMesh(mesh)
                elif obj.type.name == "TextAsset":
                    text = obj.read()
                    self.SaveText(text)
                elif obj.type.name == "MonoBehaviour":
                    mono = obj.read()
                    self.SaveMono(mono)
                elif obj.type.name == "Shader":
                    shader = obj.read()
                    print(type(shader))
                    self.SaveShader(shader)
                #else:
                    #print(obj.type)



def Usage(argv):
    #UsageMessage = os.path.basename(__file__) + ' -i <input> -o <outputpath>'

    inp = '/Users/wangcl/Desktop/unitytest/resources.assets'
    outDir = '/Users/wangcl/Desktop/untiyresource'
    filterConfig = None
    unpacker = UnPackUnityAsset(inp, outDir)
    if filterConfig == None:
        unpacker.UnPack()
    else:
        unpacker.UnPack(filterConfig)
        
    # return;
    # try:
    #     opts, args = getopt.getopt(argv, "hi:o:f:")
    # except getopt.GetoptError:
    #     print(UsageMessage)
    #     sys.exit(2)

    # for opt, arg in opts:
    #     if opt == "-h":
    #         print(UsageMessage)
    #         sys.exit()
    #     elif opt in ("-i"):
    #         inp = arg
    #     elif opt in ("-o"):
    #         outDir = arg
    #     elif opt in ("-f"):
    #         filterConfig = arg

    # if '' == inp or '' == outDir:
    #     print(UsageMessage)
    #     sys.exit(2)

    # unpacker = UnPackUnityAsset(inp, outDir)
    # if filterConfig == None:
    #     unpacker.UnPack()
    # else:
    #     unpacker.UnPack(filterConfig)


if __name__ == "__main__":
    Usage()