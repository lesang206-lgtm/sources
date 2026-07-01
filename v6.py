import os, re, uuid, shutil, zipfile, io, sys, traceback
from lxml import etree as ET
import xml.dom.minidom as minidom

try:
    import pyzstd
    from colorama import Fore, Style, init
    init(autoreset=True)
except:
    os.system('pip install pyzstd==0.15.4 colorama lxml')
    import pyzstd
    from colorama import Fore, Style, init
    init(autoreset=True)

_ZSTD_DICT = b'7\xa40\xec\xe7UC\x0bM\x10@\xae\xa6\xe9P\xaa\xffPL\x8d\xe1Tn)\xb7Dr\xbb\xecH\xaclT)(((((\xa0\xa2\xa0CU(G\x01\x18\x08r\x18\x11\x11\x9a]k\xd3\x8a:\x16\xa9\x89\xe8%\xc2\xde{\xef\xbd\xa5\x8e\xae\xdb2\xaa\x8ee\x99\x85a\xf0\xf9\xf1#\x9b\x02\x83\x05\x19\x0c\x08\x06\x05b\xa1`\x96\xc6\x81\xac}\x04D\xe4\xe1\xa4\xc3\x01\xe2`A\xc1\xe0`\xc1\xa0\xc0\xa0`0\x10\x08\x03\xc3\xc0@(\x10\x06\x80\xc2\xc2@ \x1c\n\x07D\x82\xf48\xe9\x96\x1b\x00\xd4\x0e\x11\x06\x1d\x8bA\x901\xc6\x18bH\x19\x00 \x00\x00\x00\x00\x01\x00\x00\x00\x04\x00\x00\x00\x08\x00\x00\x00mName="" useRefParam="false"/>\n\t\t\t\t<Enum name="checkOPType" value="3" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xb8\x8d\xe6\xaf\x94\xe8\xbe\x83"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="skillCombineLevel" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="skillCombineSrcId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCheckSkillMark" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration14" eventType="HitTriggerDuration" guid="38f874e2-e64b-478d-be55-fc7453046e1c" enabled="true" refParamName="" useRefParam="false" r="0.183" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="8" guid="1b06b263-6aa9-4007-a2cb-116a920b9312" status="true"/>\n\t\t\t<Event eventName="HitTriggerDuration" time="0.200" lenid="42a1f1d4-ad56-4ce4-98a3-e8d44d584741" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="alsoStopNotStartedTrack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="StopTrack0" eventType="StopTrack" guid="8013dc81-a485-4567-bc08-9e0ec7d7cd99" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.017" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="4" guid="42a1f1d4-ad56-4ce4-98a3-e8d44d584741" status="true"/>\n\t\t\t<Event eventName="StopTrack" time="0.000" isDuration="false">\n\t\t\t\t<TrackObject name="trackId" id="0" guid="c890e4ed-8300-4e21-8d66-757283ec3cc0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="alsoStopNotStartedTrack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="StopTrack1" eventType="StopTrack" guid="8633109d-53e5-4931-87b1-bf3472773aed" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.633" exe\t\t\t<uint name="\xe7\x89\xb9\xe6\xae\x8a\xe6\x95\x88\xe6\x9e\x9c\xe8\xb0\xa6\xe8\xae\xa9"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe6\x94\xb6\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe8\x87\xaa\xe6\x9d\x80"/>\n\t\t\t\t\t<uint name="\xe6\xb6\x88\xe9\x99\xa4\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\xbb\xb6\xe8\xbf\x9f\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="Buff\xe6\x88\x96\xe5\x8d\xb0\xe8\xae\xb0\xe5\xbf\xab\xe7\x85\xa7"/>\n\t\t\t\t\t<uint name="\xe6\x81\xa2\xe5\xa4\x8dBuff\xe6\x88\x96\xe5\x8d\xb0\xe8\xae\xb0\xe5\xbf\xab\xe7\x85\xa7"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe5\xb0\x84\xe7\xa8\x8b"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="CheckSkillCombineConditionTick1" eventType="CheckSkillCombineConditionTick" guid="bc7f4540-c6d9-4813-88cb-990e1d8abf7f" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.433" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="CheckSkillCombineConditionTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCurrentBuffId" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="skillCombineId" value="136001" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="checkOPType"ame="" useRefParam="false" />\r\n\t\t\t\t<bool name="forbidEnergyRecover" value="false" refParamName="" useRefParam="false" />\r\n\t\t\t\t<bool name="forbidMoveButRotate" value="false" refParamName="" useRefParam="false" />\r\n\t\t\t\t<int name="rotateSpeed" value="720" refParamName="" useRefParam="false" />\r\n\t\t\t\t<bool name="forbidCollisionDetection" value="false" refParamName="" useRefParam="false" />\r\n\t\t\t</Event>\r\n\t\t</Track>\r\n\t\t<Track trackName="PlayAnimDuration0" eventType="PlayAnimDuration" guid="4abae504-d3a2-4370-a0a8-255fde6c84d5" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.700" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n\t\t\t<Condition id="0" guid="efdb163c-b41c-4d39-b682-49e0e463281a" status="true" />\r\n\t\t\t<Event eventName="PlayAnimDuration" time="0.000" length="0.500" isDuration="true">\r\n\t\t\t\t<TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false" />\r\n\t\t\t\t<String name="clipName" value="Hit" refP/Languages/EN_Tencent_EU/image/smallbag/1005.png\x00X\x00\x00\x00https://image.ngame.proximabeta.com/eoa/Languages/EN_Tencent_EU/image/smallbag/1005.png\x00X\x00\x00\x00https://image.ngame.proximabeta.com/eoa/Languages/EN_Tencent_EU/image/smallbag/1005.png\x00\xbb\x01\x00\x00J\x00\x00\x00\x17\x00\x00\x00Terms_Of_Service_Title\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8b\x99\xe6\xa2\x9d\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\x1c\x00\x00\x00\xc4\x90i\xe1\xbb\x81u kho\xe1\xba\xa3n d\xe1\xbb\x8bch v\xe1\xbb\xa5\x00=\x00\x00\x00\xe0\xb9\x80\xe0\xb8\x87\xe0\xb8\xb7\xe0\xb9\x88\xe0\xb8\xad\xe0\xb8\x99\xe0\xb9\x84\xe0\xb8\x82\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3\xe0\xb9\x83\xe0\xb8\xab\xe0\xb9\x89\xe0\xb8\x9a\xe0\xb8\xa3\xe0\xb8\xb4\xe0\xb8\x81\xe0\xb8\xb2\xe0\xb8\xa3\x00\x11\x00\x00\x00\xec\x84\x9c\xeb\xb9\x84\xec\x8a\xa4 \xec\x95\xbd\xea\xb4\x80\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\x12\x00\x00\x00Ketentuan Layanan\x00\r\x00\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\x00\r\x00\x00\x00\xe5\x88\xa9\xe7\x94\xa8\xe8\xa6\x8f\xe7\xb4\x84\x00g\x13\x00\x00K\x00\x00\x00\x16\x00\x00\x00Terms_Of_Service_Text\x00\x15\x01\x00\x00\xe6\x9c\x8d\xe5\x8a\xa1\xe6\x9d\xa1\xe6\xac\xbe\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\xe5\x86\x85\xe5\xae\xb9\x00\x15\x01\x00\x00\xe6\x9c\x8d\xe5\x8b\x99\xe6\xa2\x9d\xe6\xac\xbe\xe5\x85\xa7\xe5\xae\xb9\xe5\x85\xa7\xe5\xae\xb9\xe5\xbc\x89"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="collisionCheckDistanceOffset" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="collisionCheckWidth" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInteruptOtherMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bProtectInteruptedByOtherMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsAreaLimitedToBeMoveDone" value="true" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SpawnObjectDuration0" eventType="SpawnObjectDuration" guid="d7e3a6f9-943b-4dda-9650-7a88a29698f8" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.783" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SpawnObjectDuration" time="0.233" length="0.300" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="bullet" id="2" isTemp="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="parentId" ob\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x01\x00\x00^KL\x00\x14\x00\x00\x000AF0A00F2605E9BB_##\x00\x00\x00\x14\x00\x00\x00349C21E70FD859FE_##\x00\x01\x00\x00\x00\x00\xe7.\x00\x00\x01\x00\x00\x00\x00\x04\x04\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x00\x90\x01\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\n\x00\x00\x00}\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\xa0\x00\x00\x00\x00\xbc\x96\x98J\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x01\x00\x00`KL\x00\x14\x00\x00\x00B8FA881B79F41C0F_##\x00\x00\x00\x14\x00\x00\x0085F89A39568DD08B_##\x00\x01\x00\x00\x00\x00`KL\x00\x01\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x00b\x00\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x0f\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x12\x01\x00\x00_KL\x00\x14\x00\x00\x004BF61216E72F555D_##\x00\x00\x00\x14\x00\x00\x00EA1631C678E20D11_##\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x12\x00\x00\x00starguardcard.png\x00\x04\x16\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x002\x00\x00\x00\xfa\x00\x00\x00d\x00\x00\x00d\x00\x00\x00\n\x00\x00\x00\x14\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00\x00\x80A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x01\x00\x00@\x85:\xe1\\\x12\x00\x00@\xeb<\r\xa5\x12\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x01\x00\x00\x05^\x0c\x00\x14\x00\x00\x00DEC1050D07839DB7_##\x00\x00\x00\x14\x00\x00\x00F620F03B6DE88773_##\x00\x01\x00\x00\x00\x00\xfa\x97\x04\x00\x01\x00\x00\x00\x00\x04\n\x01\x00\x00\x00\x00\xe7\x03\x00\x00\x88\x13\x00\x00 \x01\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\x0f\'\x00\x00\xa4\x04\x00\x00 \x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\x00\x00\xd2B\x00\x00\x80?\x00\x00\x00\x00\x00\x00\xe5\xa4\x96\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x9a\xb4\xe5\x87\xbb\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x99\x90\xe5\x88\xb6\xe6\x9c\x80\xe5\xa4\xa7\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe8\x87\xb4\xe5\x91\xbd\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe7\xa6\x81\xe7\x94\xa8\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\x9a\xb4\xe5\x87\xbb\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe8\x83\xbd\xe9\x87\x8f\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\x8a\xa4\xe7\x94\xb2\xe7\xa9\xbf\xe9\x80\x8f\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\xb3\x95\xe6\x9c\xaf\xe7\xa9\xbf\xe9\x80\x8f\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe6\x94\xbb\xe5\xb8\xa6\xe6\xb3\x95\xe6\x9c\xaf\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe8\x84\xb1\xe7\xa6\xbb\xe6\x88\x98\xe6\x96\x97\xe6\x8f\x90\xe9\x80\x9f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x9b\xbe\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x94\xb2\xe5\x87\x8f\xe4\xbc\xa4\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe7\x94\x9f\xe5\x91\xbd\xe4\xbd\x8e\xe6\x97\xb6\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe8\x87\xb4\xe7\x9b\xb2\xef\xbc\x88\xe7\xa6\x81\xe6\xad\xa2\xe4\xbd\xbf\xe7\x94\xa8\xef\xbc\x89"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe9\x99\xa4\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe9\x87\x91\xe5\xb8\x81\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\xa2\xab\xe5\x8a\xa8\xe6\x8a\x80\xe8\x83\xbd\xe5\x8f\x82\xe6\x95\xb0"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe7\x8b\x82\xe6\x84\x8f\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe7\x8e\xb0\xe5\xbd\xa2\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe8\x83\xbd\xe9\x87\x8f\xe5\x8d\xe7\xba\xbf\xe5\x8e\x8b\xe5\x8a\x9b\xef\xbc\x9b\\n\\n\xe2\x80\xa6\xe2\x80\xa6\\n\\n\xe4\xba\xba\xe7\xb1\xbb\xe7\x9a\x84\xe5\xbc\xba\xe8\x80\x85\xe4\xbb\xac\xe7\xbb\x93\xe6\x9d\x9f\xe4\xba\x86\xe5\x90\x84\xe8\x87\xaa\xe4\xb8\xba\xe6\x88\x98\xe7\x9a\x84\xe6\x97\xa5\xe5\xad\x90\xef\xbc\x8c\xe4\xbb\x96\xe4\xbb\xac\xe8\x81\x9a\xe9\x9b\x86\xe5\x9c\xa8\xe8\x90\xa8\xe5\xb0\xbc\xe7\x9a\x84\xe9\xba\xbe\xe4\xb8\x8b\xef\xbc\x8c\xe5\xb0\x86\xe4\xb8\x80\xe8\x82\xa1\xe8\x82\xa1\xe5\xbe\xae\xe5\xb0\x8f\xe7\x9a\x84\xe5\x8a\x9b\xe9\x87\x8f\xef\xbc\x8c\xe8\x81\x9a\xe5\x90\x88\xe6\x88\x90\xe6\x8e\xa8\xe5\x8a\xa8\xe5\x8e\x86\xe5\x8f\xb2\xe7\x9a\x84\xe6\xb4\xaa\xe6\xb5\x81\xe3\x80\x82\xe5\x9c\xa8\xe8\xbf\x99\xe8\x82\xa1\xe6\xb4\xaa\xe6\xb5\x81\xe9\x9d\xa2\xe5\x89\x8d\xef\xbc\x8c\xe5\xbc\xba\xe5\xa4\xa7\xe7\x9a\x84\xe6\x81\xb6\xe9\xad\x94\xe5\x8f\xaa\xe8\x83\xbd\xe9\x80\x80\xe5\xae\x88\xe6\xb7\xb1\xe6\xb8\x8a\xef\xbc\x8c\xe7\x8b\x82\xe9\x87\x8e\xe7\x9a\x84\xe5\x85\xbd\xe7\xbe\xa4\xe5\xad\xa6\xe4\xbc\x9a\xe4\xba\x86\xe8\x87\xaa\xe6\x88\x91\xe6\x94\xb6\xe6\x95\x9b\xef\xbc\x8c\xe5\xb0\xb1\xe8\xbf\x9e\xe5\x9c\xa3\xe6\xae\xbf\xe7\x9a\x84\xe7\xa5\x9e\xe7\xa5\x87\xe4\xbb\xac\xe4\xb9\x9f\xe4\xb8\x8d\xe6\x95\xa2\xe7\x9b\xb4\xe6\x8e\xa0\xe9\x94\x8b\xe8\x8a\x92\xe3\x80\x82\xe4\xbd\x86\xe8\x90\xa8\xe5\xb0\xbc\xe5\xb9\xb6\xe6\xb2\xa1\xe6\x9c\x89\xe8\xa2\xab\xe8\x87\xaa\xe5\xb7\xb1\xe7\x9a\x84\xe4\xbc\x9f\xe5\xa4\xa7\xe5\x8a\x9f\xe7\xbb\xa9\xe5\x86\xb2\xe6\x98\x8f\xe5\xa4\xb4\xe8\x84\x91\xef\xbc\x8c\xe4\xbb\x96\xe6\x97\xb6\xe5\x88\xbb\xe4\xbf\x9d\xe6\x8c\x81\xe7\x9d\x80\xe8\xad\xa6\xe6\x83\x95\xef\xbc\x8c\xe5\x8f\xaa\xe8\xa6\x81\xe6\x88\x98\xe6\x96\x97\xe7\x9a\x84\xe5\x8f\xb7\xe8\xa7\x92\xe5\x90\xb9\xe5\x93\x8d\xef\xbc\x8c\xe4\xbb\x96\xe5\xb0\xb1\xe4\xbc\x9a\xe5\x86\x8d\xe6\xac\xa1\xe6\x8c\xba\xe5\x89\x91\xe8\x80\x8c\xe4\xb8\x8a\xe3\x80\x82\\n\\n\xe2\x80\x9c\xe5\x90\xbe\xe6\x89\xa7\xe5\x90\xbe\xe5\x89\x91\xef\xbc\x8c\xe6\x96\xa9\xe5\xb0\xbd\xe5\xa5\xb8\xe9\x82\xaa\xef\xbc\x81\xe2\x80\x9d\r\n0588A320CABA3789_## = \xe7\x81\xb5\xe7\x81\xb5\xe4\xb8\xba\xe4\xbb\x80\xe4\xb9\x88\xe6\x98\xaf\xe7\x88\x86\xe7\x82\xb8\xe5\xa4\xb4\xef\xbc\x9f\r\n0590EDDF3CC30F2A_## = \xe5\xb9\xb4\xe8\xbd\xbb\xe4\xba\xba\xef\xbc\x8c\xe4\xbd\xa0\xe7\x9a\x84\xe8\xaf\x9a\xe6\x84\x8f\xe6\x89\x93\xe5\x8a\xa8\xe4\xba\x86\xe6\x88\x91\\n\xe5\xa6\x82\xe6\x9e\x9c\xe4\xbd\xa0\xe4\xb8\x8d\xe4\xbb\x8b\xe6\x84\x8f\xe5\x92\x8c\xe6\x88\x91\xe4\xb8\x80\xe8\xb5\xb7\\n\xe8\xa1\x8c\xe4\xbe\xa0\xe6\xad\xa3\xe4\xb9\x89\xef\xbc\x8c\xe9\x99\xa4\xe6\x81\xb6\xe6\x89\xac\xe5\x96\x84\\n\xe5\x88\x9a\xe5\xa5\xbd\xe6\x88\x91\xe7\x8e\xb0\xe5\x9c\xa8\xe7\xbc\xba\xe4\xb8\x80\xe4\xb8\xaa\xe5\x8a\xa9\xe7\x90\x86\\n\xe4\xbb\x8a\xe5\x90\x8e\xe6\x88\x91\xe4\xbb\xac\xe5\xb0\xb1\xe6\x98\xaf\xe6\x97\xa0\xe6\x95\x8c\xe7\x9a\x84\xe9\x9c\xb9\xe9\x9b\xb3\xe7\xbb\x84\xe5\x90\x88\xef\xbc\x81\r\n0592D198A67E021F_## = <color=#ffd200>\xe8\xa7\xa3\xe9\x94\x81\xe6\x9d\xa1\xe4\xbb\xb6</color>\xef\xbc\x9a\xe4\xb8\x8e<color=#ffd200>{0}</color>\xe8\xbe\xbe\xe5\x88\xb0<color=#ffd200>\xe7\xbe\x81\xe7\xbb\x8a\xe9\x98\xb6\xe6\xae\xb52 \xe7\x9b\xb8\xe8\xaf\x86</color>\r\n05A181D7672725DC_## = \xe6\xb4\x9b\xe9\x87\x8c\xe6\x98\x82\r\n05A9BBD41D0A9179_## = \xe2\x80\x9c\xe4\xb9\x9d\xe5\xa4\xa9\xe4\xb9\x8b\xe4\xb8\x8a\xef\xbc\x8c\xe7\xa5\x9e\xe5\xba\xa7\xe4\xb9\x8b\xe6\x97\x81\xef\xbc\x8c\xe5\x85\xad\xe7\xbf\xbc\xe8\x88\x9e\xe5\x8a\xa8\xef\xbc\x8c\xe4\xbb\xa5\xe7\xbf\xb1\xe4\xbb\xa5\xe7\xbf\x94\xe3\x80\x82\xe2\x80\x9d\\n\\n\xe8\xb8\xba\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91\xe5\xae\x83"/>\n\t\t\t\t\t<uint name="\xe4\xbd\x9c\xe4\xb8\xba\xe6\x97\x8b\xe8\xbd\xac"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="modifyDirection" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="yRotation" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="direction" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseRecordDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bChangeMaterialWithParent" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="materialParentActorId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyScaling" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="scaling" x="1.000" y="1.000" z="1.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableLayer"head145.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x15\xf6\x99\x00\x0c\x00\x00\x00vp12003.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00:\x00\x00\x00\x0f\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x16\xf6\x99\x00\x0c\x00\x00\x00vp10042.png\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00X\x00\x00\x00\x0f\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x17\xf6\x99\x00\x1b\x00\x00\x00vp-random-hero-piece_2.png\x00\x1b\x00\x00\x00vp-random-skin-piece_2.png\x00\x01\x00\x00\x00\x00I\x00\x00\x00\x0f\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x18\xf6\x99\x00\x0c\x00\x00\x00vp12003.png\x00\x1b\x00\x00\x00vp-random-hero-piece_2.png\x00\x01\x00\x00\x00\x00O\x00\x00\x00\x0f\x00\x00\x00\n\x00\x00\x00\xab\x9e\x98\x00\x1b\x00\x00\x00vp-random-hero-piece_2.png\x00\x19\xf6\x99\x00\x12\x00\x00\x00return_js_new.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00I\x00\x00\x00\x0f\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1a\xf6\x99\x00\x1b\x00\x00\x00vp-random-skin-piece_2.png\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1b\xf6\x99\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\r\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1c\xf6\x99\x00\x0c\x00\x00\x00vp90007.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00;\x00\x00\x00\x0f\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1d\xf6\x99\x00\x0c\x00\x00\x00vp10106.png\x00\r\x00\x00\x00vp120100.png\x00\x01\x00\x00\x00\x00>\x00\x00\x00\x0f\x00\x00\x00\x0f\x00\x00\x00\xac\x9e\x98\x00\x0c\x00\x00\x00vp90005.png\x00\x1e\xf6\x99\x00\x10\x00\x00\x00valorpass03.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x1f\xf6\x99\x00\x0c\x00\x00\x00vp12007.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00/\x00\x00\x00\x0f\x00\x00\x00\x11\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00 \xf6\x99\x00\x0c\x00\x00\x00vp11029.png\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00;\x00\x00\x00\x0f\x00\x00\x00\x12\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00!\xf6\x99\x00\r\x00\x00\x00vp120100.png\x00\x0c\x00\x00\x00vp90005.png\x00\x01\x00\x00\x00\x00;\x00\x00\x00\x0f\x00\x00\x00\x13\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00"\xf6\x99\x00\x0c\x00\x00\x00vp12003.png\x00\r\x00\x00\x00vp120100.png\x00\x01\x00\x00\x00\x00Q\x00\x00\x00\x0f\x00\x00\x00\x14\x00\x00\x00\xad\x9e\x98\x00\x0c\x00\x00\x00vp90007.png\x00#\xf6\x99\x00\x14\x00\x00\x00level20skin_big.png\x00\x01\x00\x00\x00\x00\x10\x00\x00\x00level20skin.png\x00;\x00\x00\x00\x0f\x00\x00\x00\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\xe7\x8e\x84\xe7\xad\x96\xe8\xa2\xab\xe5\x8a\xa8\x00\x16\x00\x00\x00\xe5\x87\xbb\xe6\x9d\x80\xe6\x88\x96\xe5\x8a\xa9\xe6\x94\xbb\xe8\x8b\xb1\xe9\x9b\x84\x007\x00\x00\x00Prefab_Characters/Prefab_Hero/195_BaiLiXuanCe/skill/P2\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\xbe\x00\x00\x00(<\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x19\x00\x00\x00\xe5\x8f\xb6\xe5\xa8\x9c\xe5\xad\xa6\xe4\xb9\xa0\xe5\xa4\xa7\xe6\x8b\x9b\xe8\xa2\xab\xe5\x8a\xa8\x00\x01\x00\x00\x00\x004\x00\x00\x00Prefab_Characters/Prefab_Hero/154_HuaMuLan/skill/P1\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\xce\x00\x00\x00%\xd5\x01\x00\xd0\x07\x00\x00\x00\x00\x00\x00\x00\x11\x00\x00\x00[EX]\xe7\x99\xbd\xe8\xb5\xb7\xe8\xa2\xab\xe5\x8a\xa8\x00\x13\x00\x00\x00\xe5\x8f\x97\xe5\x87\xbb\xe6\x9c\x89\xe5\x87\xa0\xe7\x8e\x87\xe8\xbd\xac\x00:\x00\x00\x00Prefab_Characters/Prefab_Hero/120_BaiQi/skill/extend/exP1\x00\x02\x00\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\xbf\x00\x00\x00\x98:\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\xe7\xba\xb3\xe5\x85\x8b\xe7\xbd\x97\xe6\x96\xaf\xe8\xa2\xab\xe5\x8a\xa8\x00\x01\x00\x00\x00\x00;\x00\x00\x00Prefab_Characters/Prefab_Hero/150_HanXin/skill/extend/exP2\x00\x08\x00\x00\x00\xa0\x0f\x00\x00\x14\x00\x00\x00\xf4\x01\x00\x00\x8c\x06\x17\x00\x98:\x00\x00\x0c\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x12\x01\x00\x00>A\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00U\x00\x00\x00\xef\xbc\x8810v10\xef\xbc\x89\xe7\x8c\xb4\xe5\xad\x90\xe6\xaf\x8f\xe6\xac\xa1\xe9\x87\x8a\xe6\x94\xbe\xe6\x8a\x80\xe8\x83\xbd\xe7\x9a\x84\xe6\x97\xb6\xe5\x80\x99\xe5\xb0\x86\xe4\xbc\x9a\xe8\x8e\xb7\xe5\xbe\x97\xe4\xb8\x80\xe4\xb8\xaa\xe6\x8a\xa4\xe7\x9b\xbe\xef\xbc\x8c\xe5\x8f\xaf\xe5\x8f\xa0\xe5\x8a\xa05\xe6\xac\xa1\x00\x12\x00\x00\x00\xe6\x82\x9f\xe7\xa9\xba[EX]\xe8\xa2\xab\xe5\x8a\xa81\x00;\x00\x00\x00Prefab_Characters/Prefab_Hero/167_WuKong/skill/extend/exP1\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x00\x00e="" r="0.517" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="CameraShakeDuration" time="2.000" length="2.000" isDuration="true">\n\t\t\t\t<bool name="useMainCamera" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="shakeRange" x="0.500" y="0.500" z="0.500" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_self" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_target" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_enemy" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="filter_allies" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="useAccumOffset" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cosDecay" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="cosDecayFactor" v\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00M\x00\x00\x00\x1f\xb2\x01\x00%\x00\x00\x00Play_SunShangXiang_VO_TiaoXin_Skin13\x00i+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00J\x00\x00\x00)\xb2\x01\x00"\x00\x00\x00Play_sunshangxiang_tiaoxin_Skin14\x00j+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00@\x00\x00\x00\x85\xb5\x01\x00\x18\x00\x00\x00Play_GongShuBan_TiaoXin\x00\xc0+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00F\x00\x00\x00\x99\xb5\x01\x00\x1e\x00\x00\x00Play_GongShuBan_TiaoXin_Skin2\x00\xc2+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00F\x00\x00\x00\xb7\xb5\x01\x00\x1e\x00\x00\x00Play_GongShuBan_TiaoXin_Skin5\x00\xc5+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00F\x00\x00\x00\xc1\xb5\x01\x00\x1e\x00\x00\x00Play_GongShuBan_TiaoXin_Skin6\x00\xc6+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00@\x00\x00\x00m\xb9\x01\x00\x18\x00\x00\x00Play_ZhuangZhou_TiaoXin\x00$,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00=\x00\x00\x00U\xbd\x01\x00\x15\x00\x00\x00Play_LiuShan_TiaoXin\x00\x88,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00?\x00\x00\x00=\xc1\x01\x00\x17\x00\x00\x00Play_GaoJianLi_TiaoXin\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00E\x00\x00\x00Q\xc1\x01\x00\x1d\x00\x00\x00Play_GaoJianLi_TiaoXin_Skin2\x00\xee,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00E\x00\x00\x00[\xc1\x01\x00\x1d\x00\x00\x00Play_GaoJianLi_TiaoXin_Skin3\x00\xef,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00<\x00\x00\x00%\xc5\x01\x00\x14\x00\x00\x00Play_JingKe_TiaoXin\x00P-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00B\x00\x00\x00M\xc5\x01\x00\x1a\x00\x00\x00Play_JingKe_TiaoXin_Skin4\x00T-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00B\x00\x00\x00W\xc5\x01\x00\x1a\x00\x00\x00Play_JingKe_TiaoXin_Skin5\x00U-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00-\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00C\x00\x00\x00o\xc6\x01\x00\x1b\x00\x00\x00Plname="bInverse" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="groupActorType" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="groupRadius" value="10000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterInTeam" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="teamHeroID" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDiffTeam" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="diffTeamHeroID" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMonsterType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="monsterTypeMask" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="soldierTypeMask" value="0" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SetBehaviourModeTick0" eventType="SetBehaviourModeTick" guid="53e062a5-ebd1-4b49-83fe-4b2026e48ae4" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.283" exe\t\t\t<Enum name="hitPoint" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe8\x83\xb8\xe9\x83\xa8"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xb4\xe9\x83\xa8"/>\n\t\t\t\t</Enum>\n\t\t\t\t<Enum name="MoveType" value="2" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe7\x9b\xae\xe6\xa0\x87"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe4\xbd\x8d\xe7\xbd\xae"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe7\x9b\xae\xe6\xa0\x87\xe4\xbd\x8d\xe7\xbd\xae"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bChargingEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="chargingDistance" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="distance" value="10000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bResetMoveDistance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="minSpeed" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="velocity" value="12000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="groundOffset" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIgnoreHeight" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="acceleration"v1f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String8\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/skill1_red\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x007\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd0\x00\x00\x00\x02\x00\x00\x00\x7f\x00\x00\x00\x06\x00\x00\x00v1m\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String?\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/prefab_organ/tower/skill1_bullet_red\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x001\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xca\x00\x00\x00\x02\x00\x00\x00y\x00\x00\x00\x06\x00\x00\x00v1g\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String9\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/makeDamage2\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00*\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xc3\x00\x00\x00\x02\x00\x00\x00r\x00\x00\x00\x06\x00\x00\x00v1`\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String2\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/A1E2\x04\x00\x00\x00\x04\x00er/New_BlueTower/skill/New_BlueTower_makeDamage\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00L\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe5\x00\x00\x00\x02\x00\x00\x00\x94\x00\x00\x00\x06\x00\x00\x00v1\x82\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringT\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/New_BlueTower/skill/New_BlueTower_A1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x99\x01\x00\x00\x0c\x00\x00\x00skillIDsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x0e\x01\x00\x00\x01\x00\x00\x00\x06\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\x9f\x00\x00\x00\x02\x00\x00\x00N\x00\x00\x00\x06\x00\x00\x00v1<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V75001\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xad\x03\x00\x00\x11\x00\x00\x00skillCombinesw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x1d\x03\x00\x00\x03\x00\x00\x00\x07\x01\x00\x01\x00\x00\x00\x00\x00\r\x00\x00\x00\xe5\xa4\xa7\xe7\xa5\x9e\xe5\x85\xb3\xe5\x8d\xa1\x00\x15\x00\x00\x00Tutorial_BGod_Design\x00\x17\x00\x00\x00ART_5V5_01_High_Artist\x00\x0c\x00\x00\x00PVP_5V5_Nav\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00~\x02\x00\x00z\x02\x00\x00{\x02\x00\x00\x7f\x02\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00t\x02\x00\x00w\x02\x00\x00x\x02\x00\x00\x80\x02\x00\x00\x81\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x02\x00\x00\x007\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x08\x00\x00\x00\x00\x00\x00e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00X\x02\x00\x00X\x02\x00\x00X\x02\x00\x00X\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0c\x00\x00\x00pvp_5_small\x00\r\x00\x00\x00pvp_5_detail\x00\n\x00\x00\x00pvp_5_big\x00g\x00\x00\x00g\x00\x00\x00g\x00\x00\x00g\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\xdd\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x02\x00\x00\x00\x98:\x00\x00\x00\x00\x00\x00\x0f\x00\x00\x00Play_PVP_Music\x00\x0f\x00\x00\x00Stop_PVP_Music\x00\x01\x00\x00\x00\x00\n\x00\x00\x00Music_PVP\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90_\x01\x00\x95_\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xd8\x02\x00\x00e\x00\x00\x00\x01\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x10\x00\x00\x00\xe5\x8f\xac\xe5\x94\xa4\xe5\xb8\x88\xe6\x88\x98\xe5\x9c\xba\x00\x15\x00\x00\x00PVE_1_1_logic_Design\x00\x18\x00\x00\x00ART_PJGC_02_High_Artist\x00\x01\x00\x00\x00\x00\x05\x00\x00\x00\n\x00\x00\x00Img_Story\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x03\x00\x00\x00\xf3\x03\x00\x00\xf4\x03\x00\x00\xf5\x03\x00\x00Q\xc3\x00\x00\x00\x00\x00\x00f\x00\x00\x00\x05M\x04\x00\x00\x05\xb1\x04\x00\x00\x05\x15\x05\x00\x00\x05{\x05\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00\t\x00\x00\x00\r\x00\x00\x00F\x05\x00\x00\xe7\x06\x00\x00\x88\x08\x00\x00\x9e\t\x00\x00\x84\x03\x00\x00\x9a\x04\x00\x00\xb0\x05\x00\x00i\x06\x00\x00\x00\x08\x00\x00\x00PVE_1_3\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfa*\x00\x00\x00\x00\x00\x00\xc9\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00\x01\x00\x00\x00o\x00\x00\x00y\x00\x00\x00\x83\x00\x00\x00\x8d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 N\x00\x00\x00\x00\x00\x00\x0ee\x00\x01\x00\x00\x00\x00E\x00\x00\x00f\x82\x17\x00\x19\x00\x00\x00Play_Yena_VOX_Come_Skin7\x00/<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00@\x00\x00\x00\xba\xa6\x17\x00\x14\x00\x00\x00Play_LuoBin_VO_Come\x00\x8c<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00D\x00\x00\x00\xca\xcd\x17\x00\x18\x00\x00\x00Play_ZhangLiang_VO_Come\x00\xf0<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00J\x00\x00\x00\xf6\xce\x17\x00\x1e\x00\x00\x00Play_ZhangLiang_VO_Come_Skin3\x00\xf3<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00J\x00\x00\x00Z\xcf\x17\x00\x1e\x00\x00\x00Play_ZhangLiang_VO_Come_Skin4\x00\xf4<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00A\x00\x00\x00\xda\xf4\x17\x00\x15\x00\x00\x00Play_BuZhiHuoWu_Show\x00T=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x00\x06\xf6\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin3\x00W=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x00j\xf6\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin4\x00X=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x00\xce\xf6\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin5\x00Y=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00G\x00\x00\x002\xf7\x17\x00\x1b\x00\x00\x00Play_BuZhiHuoWu_Show_Skin6\x00Z=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00)\x00\x00\x00\xea\x1b\x18\x00\x01\x00\x00\x00\x00\xb8=\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00)\x00\x00\x00\nj\x18\x00\x01\x00\x00\x00\x00\x80>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00B\x00\x00\x00*\xb8\x18\x00\x16\x00\x00\x00Play_Nakelulu_VO_Come\x00H?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00H\x00\x00\x00V\xb9\x18\x00\x1c\x00\x00\x00Play_Nakelulu_VO_Come_Skin3\x00K?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00Come\x00\x01\x00\x00\x00\x00H\x00\x00\x00:\xdf\x18\x00\x1c\x00\x00\x00Play_163_JuYouJing_VOX_Come\x00\xac?\x00\x01\x00\x00\x00\x00\x00?\x00\x00\x00Prefab_Skill_Effects/Level_Effects/AutoChess_Effects/ChessDrop\x00\x00\x00\x80?\x01\x00\x00\x00\x00\xb8\x0b\x00\x00\x00\x00\x00\x00\xcd\xcc\xcc=\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00MSES\x07\x00\x00\x00\x17\x00\x00\x00\x0f\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x005d388e873657b33c203ea1a6adbbd555\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x13\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x001131\x00\x02\x00\x00\x00P\x00\x13\x00\x00\x00\x02\x00\x00\x00\x05\x00\x00\x001132\x00\x02\x00\x00\x00B\x00\x12\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00901\x00\x02\x00\x00\x00C\x00\x12\x00\x00\x00\x04\x00\x00\x00\x04\x00\x00\x00902\x00\x02\x00\x00\x00D\x00\x13\x00\x00\x00\x05\x00\x00\x00\x05\x00\x00\x001130\x00\x02\x00\x00\x00E\x00\x13\x00\x00\x00\x06\x00\x00\x00\x05\x00\x00\x001133\x00\x02\x00\x00\x00F\x00\x13\x00\x00\x00\x07\x00\x00\x00\x05\x00\x00\x001134\x00\x02\x00\x00\x00G\x00\x13\x00\x00\x00\x08\x00\x00\x00\x05\x00\x00\x001135\x00\x02\x00\x00\x00H\x00\x13\x00\x00\x00\t\x00\x00\x00\x05\x00\x00\x001136\x00\x02\x00\x00\x00I\x00\x13\x00\x00\x00\n\x00\x00\x00\x05\x00\x00\x001137\x00\x02\x00\x00\x00J\x00\x13\x00\x00\x00\x0b\x00\x00\x00\x05\x00\x00\x001138\x00\x02\x00\x00\x00K\x00\x13\x00\x00\x00\x0c\x00\x00\x00\x05\x00\x00\x001139\x00\x02\x00\x00\x00L\x00\x13\x00\x00\x00\r\x00\x00\x00\x05\x00\x00\x001180\x00\x02\x00\x00\x00M\x00\x13\x00\x00\x00\x0e\x00\x00\x00\x05\x00\x00\x001181\x00\x02\x00\x00\x00N\x00\x13\x00\x00\x00\x0f\x00\x00\x00\x05\x00\x00\x001183\x00\x02\x00\x00\x00O\x00MSES\x07\x00\x00\x00\x82\x01\x00\x00a\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e7c2b766e9bca08f64db4f0b283f3ce4\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\xd6\x00\x00\x00i\x00\x00\x00\x14\x00\x00\x0096C81CC5CA834D6C_##\x00\x1f\x00\x00\x00WrapperAI/Hero/HeroAutoChessAI\x00\xa0(\x00\x00\x00\x00\x00\x00LO\x00\x00\x00\x00\x00\x00\x02\x00\x01\x00\x02\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00$\x00\x00\x00Actions/SysEvent/PVP_AutoChess/Born\x00\x01\x00\x00\x00\x00)\x00\x00\x00Actions/SysEvent/PVP_AutoChess/Dead_Born\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfa\x00\x00\x00j\x00\x00\x00\x14\x00\x00\x000D17FEB38CC06\x00\x00\x00\x04\x00\x00\x00&\x01\x00\x00\x12\x00\x00\x00iCollisionSize&\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x11\x00\x00\x00\x08\x00\x00\x00TypeVInt3\x04\x00\x00\x00\xe6\x00\x00\x00\x03\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00x9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V500\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00y9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V400\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00z9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V400\x04\x00\x00\x00\x04\x00\x00\x00W\x00\x00\x00\x11\x00\x00\x00iBulletHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V1200\x04\x00\x00\x00\x04\x00\x00\x00t\x00\x00\x00\x12\x00\x00\x00BtResourcePathV\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String(\x00\x00\x00\x05\x00\x00\x00VWrapperAI/Hero/HeroCommonAutoAI\x04\x00\x00\x00\x04\x00\x00\x00\x85\x00\x00\x00\x0f\x00\x00\x00deadAgePathj\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String<\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/542_Tachi/skill/Death\x04\x00\x00\x00\x04\x00\x00\x00PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA\x00\x00\x00\x00Prefab_Hero/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA*\x00\x00\x00Prefab_Hero/542_Tachi/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\xab%\xb5\xdc\x86\x1c\x00\x00\x86\x1c\x00\x00/\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81^\x00\x00\x00Prefab_Hero/542_Tachi/542_Tachi_actorinfo.bytesPK\x05\x06\x00\x00\x00\x00\x03\x00\x03\x00\xdb\x00\x00\x001\x1d\x00\x00\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00121_MiYue/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00121_MiYue/skill/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1a\x00\x00\x00121_MiYue/skill/AutoChess/PK\x03\x04RefParam="false"/>\n\t\t\t\t<bool name="bBulletPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="lookTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAlwaysLookTarget" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bLookTarget" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBullerPosDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="b1stTickParentRot" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bHideWhenDead" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotateFollowCamera" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIgnoreWhenHideModel" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUse3DUICamerang name="tag" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="sightRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSameVisibleAsAttacker" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bVisibleByFow" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkinAdvance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="visionActorId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRefreshVision" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForbidBulletInObstacle" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForbidTargetOutOfNavmeshConvexHull" va\x00\x19\x00\x00\x00particlesInFirstLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\x06\x05\x00\x00\x04\x00\x00\x00\x1e\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xb7\x00\x00\x00\x02\x00\x00\x00f\x00\x00\x00\x06\x00\x00\x00v1T\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String&\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/commonempty\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00F\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdf\x00\x00\x00\x02\x00\x00\x00\x8e\x00\x00\x00\x06\x00\x00\x00v1|\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringN\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/129_dianwei/dianwei_attack_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00M\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe6\x00\x00\x00\x02\x00\x00\x00\x95\x00\x00\x00\x06\x00\x00\x00v1\x83\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringU\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/129_dianwei/dianwei_attack02_spell01\x04\x00\x00P\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x004EEC4F2E66D84324_##\x00\x14\x00\x00\x0022CA5E1185A20996_##\x00\n\x00\x00\x0011084.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xa2\x00\x00\x00\\R\x00\x00\x02\x00\x01\x01=\x00\x00\x00Prefab_Skill_Effects/Inner_Game_Effect/kill/Kill_78_bleachVP\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x009C5DF28AAE7D3EE2_##\x00\x14\x00\x00\x00D24D8A620C89E63A_##\x00\n\x00\x00\x0021084.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xa6\x00\x00\x00ly\x00\x00\x03\x00\x01\x01A\x00\x00\x00Prefab_Skill_Effects/Inner_Game_Effect/sprint/sprint_78_bleachVP\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x00849FC2788990326B_##\x00\x14\x00\x00\x00E94BDB26D3AF7FEB_##\x00\n\x00\x00\x0031084.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xa5\x00\x00\x00M+\x00\x00\x01\x00\x01\x01@\x00\x00\x00Prefab_Skill_Effects/Inner_Game_Effect/returncity/return_5V5_01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x14\x00\x00\x00ACA13FE146E55BC7_##\x00\x14\x00\x00\x00F3CFA939C7E48289_##\x00\n\x00\x00\x0011085.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xc9\x00\x00\x00*\xa0\x00\x00\x04\x00\x01\x011\x00\x00\x00Prefab_Skill_Effects/Emoji_Effect/Emoji_houyi_01\x00\x00\x00\x00\x00\x18\x00\x00\x00Play_Emoji_GeneralPopup\x00\x1d\x00\x00\x00Play_Emoji_GeneralPopup_Down\x00\x14\x00\x00\x009DF7DA730FC32408_##\x00\x14\x00\x00\x00559A118E1D79C256_##\x00\n\x00\x00\x0041002.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xc7\x00\x00\x00+\xa0\x00\x00\x04\x00\x01\x01/\x00\x00\x00Prefab_Skill_Effects/Emoji_Effect/Emoji_jin_01\x00\x00\x00\x00\x00\x18\x00\x00\x00Play_Emoji_GeneralPopup\x00\x1d\x00\x00\x00Play_Emoji_GeneralPopup_Down\x00\x14\x00\x00\x0084D3846A3B38B40D_##\x00\x14\x00\x00\x00D3B4AFBD692854AB_##\x00\n\x00\x00\x0041003.png\x00\x01\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x01\xc8\x00\x00\x00,\xa0\x00\x00\x04\x00\x01\x010\x00\x00\x00Prefngle name="randRotEnd" x="0.000" y="0.000" z="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseTargetSkinEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="7d755f67-9943-4d08-b439-ce9215f3a028" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.417" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SpawnBulletTick" time="0.200" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="targetPosActorId" objectName="None" id="-1" isTemp="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="referenceObjectId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="ActionName" value="prefab_characters/prefab_hero/190_zhugeliang/skill/AutoChess/aca1b1" refvalue="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSpecialBuffEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bActionCtrlObjs" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bLayOnNavMesh" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleSelf" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleEnemy" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleTeamNotSelf" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="syncAnimationName" value="" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="MoveBulletDuration0" eventType="MoveBulletDuration" guid="a4b4420f-87ae-4a8f-8c74-f5b800394aec" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.367" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="MoveBulletDuration" time="0.000" length="0.533" isDpeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V50002\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x06\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\x9f\x00\x00\x00\x02\x00\x00\x00N\x00\x00\x00\x06\x00\x00\x00v1<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V50000\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xe4\x01\x00\x00\x19\x00\x00\x00particlesInFirstLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00L\x01\x00\x00\x01\x00\x00\x00D\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdd\x00\x00\x00\x02\x00\x00\x00\x8c\x00\x00\x00\x06\x00\x00\x00v1z\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringL\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/Common_Effects/EF_PVP_M_11DefenseTower_Blue_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00)\x03\x00\x00\x1d\x00\x00\x00hurtParticlesInOtherLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\x8d\x02\x00\x00\x02\x00\x00\x00B\x01\x00\x00t name="\xe5\xa2\x9e\xe5\x8a\xa0\xe9\x87\x91\xe9\x92\xb1\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\x8b\xb1\xe9\x9b\x84\xe7\x94\x9f\xe5\x91\xbd\xe6\x97\xb6\xe9\x95\xbf"/>\n\t\t\t\t\t<uint name="\xe7\xa6\xbb\xe5\xbc\x80\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85\xe4\xb8\x80\xe5\xae\x9a\xe8\x8c\x83\xe5\x9b\xb4\xe5\x90\x8e\xe6\xb8\x85\xe9\x99\xa4BUFF"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe7\x9b\xae\xe6\xa0\x87\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90"/>\n\t\t\t\t\t<uint name="\xe9\x99\xa4\xe7\x9b\xae\xe6\xa0\x87\xe5\xa4\x96\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe9\x80\x9f\xe6\x8a\xb5\xe6\x8a\x97"/>\n\t\t\t\t\t<uint name="\xe8\xa7\xa3\xe9\x99\xa4\xe5\x87\x8f\xe9\x80\x9f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\xad\xbb\xe4\xba\xa1"/>\n\t\t\t\t\t<uint name="\xe8\x83\xbd\xe9\x87\x8f\xe6\xb6\x88\xe8\x80\x97\xe5\x89\x8a\xe5\x87\x8f"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe8\xb6\xb3\xe7\x90\x83\xe8\x83\xbd\xe9\x87\x8f"/>\n\t\t\t\t\t<uint name="\xe7\x89\xb9\xe6\xae\x8a\xe6\x95\x88\xe6\x9e\x9c\xe5\xa5\x89\xe7\x8c\xae"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe8\x87\xaa\xe5\xae\x9a\xe4\xb9\x89\xe8\x83\xbd\xe9\x87\x8f"/>\n\t\t\t\t\t<uint name="\xe8\xa7\x92\xe8\x89\xb2\xe9\x87\x8d\xe7\x94\x9f"/>\n\t\t\t\t\t<uint name="\xe8\x83\xbd\xe9\x87\x8f\xe8\x8e\xb7\xe5\x8f\x96\xe5\x89\x8a\xe5\x87\x8f\xe6\xaf\x94\xe4\xbe\x8b"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe7\x94\x9f\xe5\x91\xbd\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe7\x94\x9f\xe5\x91\xbd\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe9\xad\x94\xe6\xb3\x95\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe9\xad\x94\xe6\xb3\x95\xe4\xba\x94\xe5\x9b\x9e"/>\n\t\t\t\t\t<uint name="\xe5\xbf\xbd\xe7\x95\xa5\xe9\x98\xb2\xe5\xbe\xa1\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xb1\x9e\xe6\x80\xa7\xe4\xba\x92\xe7\x9b\xb8\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe4\xb8\xbb\xe4\xba\xba\xe5\xb1\x9e\xe6\x80\xa7\xe8\xbd\xac\xe5\x8c\x96\xe7\xbb\x99\xe5\xae\xa0\xe7\x89\xa9"/>\n\t\t\t\t\t<uint name="\xe6\x81\x90\xe6\x83\xa7\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x99\x90\xe5\x88\xb6\xe5\x8d\x95\xe6\xac\xa1\xe4\xbc\xa4\xe5\xae\xb3\xe4\xb8\x8a\xe4\xb8\x8b\xe9\x99\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x8a\x80\xe8\x83\xbd\xe9\x80\x89\xe4\xb8\xad"/>\n\t\t\t\t\t<uint name="\xe6\xb6\x88\xe8\x80\x97\xe6\xb3\x95\xe5\x8a\x9b\xe5\x80\xbc\xe6\x8a\xb5\xe6\x8c\xa1\xe4\xbc\xa4\xe5refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxTriggerCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxSelfBuffCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxTargetBuffCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTotalHitCount" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEdgeCheck" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bExtraBuff" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_1" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_2" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_3" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TargetSkillCombine_1" value="505100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="TargetSkillLeaveRemove_1" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TargetSkillCombine_2" value="505120" refPSetAttackDirDuration0" eventType="SetAttackDirDuration" guid="13f98c0c-0c95-4e18-aeb2-1fef43e76e8b" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.333" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SetAttackDirDuration" time="0.000" length="0.050" isDuration="true">\n\t\t\t\t<TemplateObject name="attackerId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForceRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bImmediateRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ForbidAbilityDuration0" eventType="ForbidAbilityDuration" guid="70d891be-ca4c-4c49-af6f-53ed54d35f4b" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.283" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="ForbidAbilityDuration" time="0.000" length="0.200" isD name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x80\x92\xe6\xb0\x94\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe6\xb3\x95\xe7\x90\x83\xe6\xa7\xbd\xe4\xbd\x8d"/>\n\t\t\t\t\t<uint name="\xe6\xa0\xb9\xe6\x8d\xae\xe6\x8a\xa4\xe7\x94\xb2\xe5\x80\xbc\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe6\xa0\xbc\xe6\x8c\xa1\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\xa4\xa7\xe8\xa7\x86\xe9\x87\x8e\xe5\x8d\x8a\xe5\xbe\x84"/>\n\t\t\t\t\t<uint name="\xe5\x8d\x95\xe4\xb8\xaa\xe6\x8a\x80\xe8\x83\xbd\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe5\x8f\x8d\xe5\xbc\xb9"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe8\xa7\xa6\xe5\x8f\x91\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe5\xa4\x8d\xe6\xb4\xbb\xe6\x97\xb6\xe9\x97\xb4"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe8\xa7\x92\xe8\x89\xb2\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe6\xa7\xbd\xe4\xbd\x8d\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xbb\xb6\xe9\x95\xbf\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xb1\x9e\xe6\x80\xa7\xe8\xbd\xac\xe6\x8d\xa2"/>\n\t\t\t\t\t<uint name="\xe7\xb1\xbb\xe5\x9e\x8b\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x9c\x80\xe5\xa4\xa7\xe6\xb3\x95\xe5\x8a\x9b\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x9c\x80\xe5\xa4\xa7\xe6\xb3\x95\xe5\x8a\x9b\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\xae\xad\xe8\xaf\xab\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe9\x94\x90\xe6\xb0\x94\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\x85\xb1\xe4\xba\xab\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe5\x85\xb1\xe4\xba\xab\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x8f\x8d\xe5\x87\xbb\xe6\x99\xae\xe6\x94\xbb\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe5\x89\x8d\xe8\xb0\x83\xe6\x95\xb4\xe5\x8f\x97\xe5\x88\xb0\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe5\x89\x8d\xe8\xb0\x83\xe6\x95\xb4\xe9\x80\xa0\xe6\x88\x90\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe8\x83\x8c\xe5\x90\x8e\xe6\x94\xbb\xe5\x87\xbb\xe6\x9a\xb4\xe5\x87\xbb"/>\n\t\t\t\t\t<uint name="\xe6\x9a\xb4\xe5\x87\xbb\xe7\x8e\x87\xe8\xbd\xac\xe5\x8c\x96\xe6\x9a\xb4\xe5\x87\xbb\xe4\xbc\xa4\xe5\xae\xb3 name="excuteMoveCmd" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="immediaRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="PlayMSES\x07\x00\x00\x00\x08\x00\x00\x00\x10\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000ed9c5e8c7fd9b42e102b09260202589\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00`\xea\x00\x00\x04\x00\x00\x00a\xea\x00\x00\x04\x00\x00\x00b\xea\x00\x00\x04\x00\x00\x00c\xea\x00\x00\x04\x00\x00\x00d\xea\x00\x00\x04\x00\x00\x00e\xea\x00\x00\x04\x00\x00\x00f\xea\x00\x00\x04\x00\x00\x00g\xea\x00\x00\x04\x00\x00\x00h\xea\x00\x00\x04\x00\x00\x00i\xea\x00\x00\x04\x00\x00\x00j\xea\x00\x00\x04\x00\x00\x00k\xea\x00\x00\x04\x00\x00\x00l\xea\x00\x00\x04\x00\x00\x00m\xea\x00\x00\x04\x00\x00\x00n\xea\x00\x00\x04\x00\x00\x00o\xea\x00\x00MSES\x07\x00\x00\x00\xb6\x00\x00\x00\x00\x01\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0024e234988d548d1822de209cfbd17add\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00|\x01\x00\x00\xe9\x03\x00\x00\x05\x00\x00\x00Body\x00\x05\x00\x00\x00Hair\x00O\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_00_D_512.tga\x00W\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_Alpha_512_Mask.bytes\x00O\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_00_D_256.tga\x00W\x00\x00\x00Characters/Hero/116_JingKe/Component/Textures/1161_JingKe_Hair_RT_Alpha_256_Mask.bytes\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00x\x01\x00\x00\xea\x03\x00\x00\x05\x00\x00\x00Body\x00\x01\x00\x00\x00\x00O\x00\x00\x00ChParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSpecifiedDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="specifiedDir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReachDestStop" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bStopOnNavEdge" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDelayLeave" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="randomRotateRange" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bKeepRelateDistance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOptimizeLanding" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDontFallInWall" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration1" eventType="HitTriggerDuration" guid="ed80eb7a-cbd8-4b36-a5da-860e3ab6f453" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.383" exeProSmall" type="int" value="5000" />\r\n    <par name="c_HideContinueSelfHP_ConSmall" type="int" value="7000" />\r\n  </pars>\r\n  <node class="SelectorLoop" version="1" id="0">\r\n    <node class="WithPrecondition" version="1" id="40">\r\n      <node class="Action" version="1" id="42">\r\n        <property Method="Self.NucleusDrive::Logic::ActorBaseAgent::IsDeadState()" />\r\n        <property PreconditionFailResult="BT_FAILURE" />\r\n        <property ResultOption="BT_INVALID" />\r\n      </node>\r\n      <node class="Sequence" version="1" id="51">\r\n        <node class="Action" version="1" id="25">\r\n          <property Method="Self.NucleusDrive::Logic::CombatAgent::SetCurrCombatDecision(Idle,32)" />\r\n          <property PreconditionFailResult="BT_FAILURE" />\r\n          <property ResultOption="BT_INVALID" />\r\n        </node>\r\n        <node class="Action" version="1" id="41">\r\n          <property Method="Self.NucleusDrive::Logic::CombatAgent::SwitchMicroTree(&quot;WrapperAI/Hierarchical/MicroAIs/HeroMicroIdelAI&quot;,true)" />\r\n="" useRefParam="false"/>\n\t\t\t\t<bool name="bForceClearSkillIndicator" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillInputCacheDuration0" eventType="SkillInputCacheDuration" guid="a74d46ba-4213-46ba-a7ec-e1f30bd87c8a" enabled="true" refParamName="" useRefParam="false" r="0.000" g="0.917" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillInputCacheDuration" time="0.000" length="0.400" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cacheSkill" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReturnCacheWhenLeaving" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceCacheSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="notForceCacheSkill0" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="notForceCacheSkill1"!\x00E/\x07\xb9T\x0e\x00\x00T\x0e\x00\x00\x1d\x00\x00\x00156_ZhangLiang/skill/A4B1.xml\xef\xbb\xbf<?xml version="1.0" encoding="utf-8"?>\r\n<Project>\r\n  <TemplateObjectList>\r\n    <TemplateObject objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" />\r\n    <TemplateObject objectName="target" id="1" isTemp="false" />\r\n    <TemplateObject objectName="bullet" id="2" isTemp="true" />\r\n  </TemplateObjectList>\r\n  <RefParamList>\r\n    <uint name="156a4b1" value="0" refParamName="" useRefParam="false" />\r\n  </RefParamList>\r\n  <Action tag="" length="5.000" loop="false">\r\n    <Track trackName="SpawnLiteObjDuration0" eventType="SpawnLiteObjDuration" guid="a108b9de-b380-464d-ad3f-97838128e929" enabled="true" refParamName="" useRefParam="false" r="0.417" g="0.000" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\r\n      <Event eventName="SpawnLiteObjDuration" time="0.000" length="3.000" isDuration="true">\r\n        <String name="OutputLiteBulletName" value="156a4b1" refParamName="" useRefParam="false" />\r\n        <uint name="ConfigID" valisDuration="false">\n\t\t\t\t<Enum name="SkillFuncType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe7\x89\xa9\xe7\x90\x86\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe7\x9c\x9f\xe5\xae\x9e\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x94\x9f\xe5\x91\xbd\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x8a\xa4\xe7\x94\xb2"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x8a\xa4\xe7\x94\xb2"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x8a\x97\xe6\x80\xa7"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x8a\x97\xe6\x80\xa7"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x8a\x80\xe8\x83\xbdCD"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x9a\xb4\xe5\x87\xbb\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x9a\xb4\xe5\x87\xbb\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x9c\x80\xe5\xa4\xa7\xe7\x94\x9f\xe5\x91\xbd"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x9c\x80\xe5\xa4\xa7\xe7\x94\x9f\xe5\x91\xbd"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\x89\xa9\xe7\x90\x86\xe7\xa9\xbf\xe9\x80\x8f"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\x89\xa9\xe7\x90\x86\xe7\xa9\xbf\xe9\x80\x8f"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe7.String\x0f\x00\x00\x00\x05\x00\x00\x00VSpell3\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\t\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xa2\x00\x00\x00\x02\x00\x00\x00Q\x00\x00\x00\x06\x00\x00\x00v1?\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\x11\x00\x00\x00\x05\x00\x00\x00VSpell3_1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00MSES\x07\x00\x00\x00\x1c\x00\x00\x00\xe0\x01\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0055da304ff85c361e25965639354f5378\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00%w\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00&w\x00\x00\x04)\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00\'w\x00\x00\xf8*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00(w\x00\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00)w\x00\x00\xe0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00*w\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00%w\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00&w\x00\x00\x04)\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00\'w\x00\x00\xf8*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00(w\x00\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00)w\x00\x00\xe0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00*w\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00%w\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00&w\x00\x00\x04)\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00\'w\x00\x00\xf8*\x00\x00\x00\x00\x00\x00\x00\x00\x00\x002\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00(w\x00\x00\xec,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00)w\x00\x00\xe0.\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00*w\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\x00\x00\x18\x00\x00\x00\x04\x00\x00\x00%w\x00\x00rRepeatedly" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="overrideCDValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="triggerRatio" value="0" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>\n\nPK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\xa0\x04\xec\x038=\x00\x008=\x00\x00\x1a\x00\x00\x00107_Zhaoyun/skill/A1E1.xml<?xml version="1.0" encoding="utf-8"?>\n<Project>\n\t<TemplateObjectList>\n\t\t<TemplateObject objectName="self" id="0" isTemp="false"/>\n\t\t<TemplateObject objectName="target" id="1" isTemp="false"/>\n\t</TemplateObjectList>\n\t<RefParamList>\n\t\t<Vector3i name="_BulletDir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t</RefParamList>\n\t<Action tag="" length="0.500" loop="false">\n\t\t<Track trackName="FilterTargetType6" eventType="FilterTargetType" guid="20f64bb4-0d0e-40ed-91b4-7ee34475407e" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.083" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="FilterTargetType" timetem.StringB\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Monster/Mst_87_Monkey/skill/M1A2\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00:\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd3\x00\x00\x00\x02\x00\x00\x00\x82\x00\x00\x00\x06\x00\x00\x00v1p\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringB\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Monster/Mst_87_Monkey/skill/A1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x009\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd2\x00\x00\x00\x02\x00\x00\x00\x81\x00\x00\x00\x06\x00\x00\x00v1o\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringA\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/PassiveResource/JungleHeal\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00;\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd4\x00\x00\x00\x02\x00\x00\x00\x83\x00\x00\x00\x06\x00\x00\x00v1q\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringC\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/prefab_hero/PassiveResource/JungleHealB1\x04\x00\x00\x00\x04\x00cts/hero_skill_effects/199_li/li_attack01_spll01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00G\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe0\x00\x00\x00\x02\x00\x00\x00\x8f\x00\x00\x00\x06\x00\x00\x00v1}\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringO\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/199_li/Li_attack_spell02_trail\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00B\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdb\x00\x00\x00\x02\x00\x00\x00\x8a\x00\x00\x00\x06\x00\x00\x00v1x\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/199_li/li_attack_spell03b\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00A\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xda\x00\x00\x00\x02\x00\x00\x00\x89\x00\x00\x00\x06\x00\x00\x00v1w\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringI\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/199_li/li_attack_spell03\x04\x00\x00\x00\x04\x00em.StringN\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/999_ChessPlayer/99940_ChessPlayer_Show2\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00~\x01\x00\x00\x10\x00\x00\x00TransConfigsK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig[]\x04\x00\x00\x00\x1b\x01\x00\x00\x02\x00\x00\x00`\x00\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00\x04\x00\x00\x00\xb3\x00\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00W\x00\x00\x00\x01\x00\x00\x00O\x00\x00\x00\t\x00\x00\x00Scale:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V1.3\x04\x00\x00\x00\x04\x00\x00\x00i\x00\x00\x00!\x00\x00\x00bShadowCameraFollowLobbyActor<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x1a\x00\x00\x00\x08\x00\x00\x00TypeSystem.Boolean\r\x00\x00\x00\x05\x00\x00\x00VTrue\x04\x00\x00\x00\x04\x00\x00\x00`\x00\x00\x00\x19\x00\x00\x00runAnimationBaseSpeed;\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\r\x00\x00\x00\x05\x00\x00\x00V0.86\x04\x00\x00\x00\x04\x00\x00\x00k\x00\x00\x00\x14\x00\x00\x00SpecialFadeTimesK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SpeicalFadeTime[]\x04\x00\x00\x00\x04\x00\x00\x00S\x00\x00\x00\r\x00\x00\x00hudHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V3000\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\x0e\x00\x00\x00LobbyScale8\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\n\x00\x00\x00\x05\x00alue="5000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID" value="11601" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID2" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID3" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID4" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseCombo" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID1Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseStop" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID2Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkillLevel" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID3Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID4Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="recoverSkillID" value="11600" ref\xe5\x87\xbb\xe6\x9d\x80\xe9\xa2\x9d\xe5\xa4\x96\xe7\xbb\x8f\xe9\xaa\x8c\x00\x02\x00\x10\'\x00\x00(#\x00\x00L\x1d\x00\x00p\x17\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x94\x11\x00\x00\x02\x00\x02\x00\x10\'\x00\x00\x10\'\x00\x00\x00\x03\x00\x02\x00\x00\x00\x00\x00\xb8\x0b\x00\x00\x00\x10\'\x00\x00c\x00\x00\x00X\x00\x00\x00\x08\x00\x00\x00\x03\x00\r\x00\x00\x00\xe8\x8c\x83\xe5\x9b\xb4\xe5\xb9\xb3\xe5\x88\x86\x00\x02\x00\x10\'\x00\x00@\x1f\x00\x00d\x19\x00\x00\x88\x13\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\x04\x00\x01\x00\x00\x00\x00\x00\x88\x13\x00\x00\x01\x03\x00\x02\x00\x00\x00\x00\x00\x10\'\x00\x00\x01\x10\'\x00\x00{\x00\x00\x00Y\x00\x00\x00\x08\x00\x00\x00\x04\x00%\x00\x00\x00\xe8\x8c\x83\xe5\x9b\xb4\xe5\x86\x85\xe5\xb9\xb3\xe5\x88\x86\xef\xbc\x8c\xe5\x87\xbb\xe6\x9d\x80\xe9\xa2\x9d\xe5\xa4\x96\xe7\xbb\x8f\xe9\xaa\x8c\x00\x02\x00\x10\'\x00\x00@\x1f\x00\x00d\x19\x00\x00\x88\x13\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\xa0\x0f\x00\x00\x02\x00\x02\x00\x10\'\x00\x00p\x17\x00\x00\x00\x03\x00\x02\x00\x00\x00\x00\x00p\x17\x00\x00\x00\x10\'\x00\x00x\x00\x00\x00Z\x00\x00\x00\x08\x00\x00\x00\x05\x00"\x00\x00\x00\xe9\x98\xb5\xe8\x90\xa5\xe5\xb9\xb3\xe5\x88\x86\xef\xbc\x8c\xe5\x8a\xa9\xe6\x94\xbb\xe9\xa2\x9d\xe5\xa4\x96\xe7\xbb\x8f\xe9\xaa\x8c\x00\x02\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x10\'\x00\x00\x01\x00\x02\x00\x00\x00\x00\x00\x10\'\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\'\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00Prefab_Hero/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00Prefab_Hero/510_Liliana/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\xe9a\x8a\x18W5\x00\x00W5\x00\x003\x00\x00\x00Prefab_Hero/510_Liliana/510_Liliana_actorinfo.bytesW5\x00\x00\x08\x00\x00\x00ROOTD\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom/\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CActorInfo\x04\x00\x00\x00\x035\x00\x00\x0e\x00\x00\x00Y\x00\x00\x00\r\x00\x00\x00ActorName@\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\x12\x00\x00\x00\x05\x00\x00\x00V\xe8\x8e\x89\xe8\x8e\x89\xe5\xae\x89\x04\x00\x00\x00\x04\x00\x00\x00\xeb\x01\x00\x00\x10\x00\x00\x00ArtPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xa3\x01\x00\x00\x03\x00\x00\x00\x89\x00\x00\x00\x0b\x00\x00\x00Elementr\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringD\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/510_Liliana/5101_Liliana_LOD1\x04\x00\x00\x00\x04\x00\x00\x00\x89\x00\x00\x00Param="false"/>\n\t\t\t\t<int name="iDelayDisappearTime" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="particleScaleGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableMaxFollowTime" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="maxFollowTime" value="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bindOnHUD" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="showInStatus" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xbb\xbb\xe6\x84\x8f\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="Idle\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe5\x8a\xa8\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe6\xad\xbb\xe4\xba\xa1\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe5\x85\xb6\xe4\xbb\x96\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe8\x84\xb1\xe6\x88\x98\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe6\x88\x98\xe6\x96\x97\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe9\x9d\x9e\xe9\x9a\x90\xe8\x97\x8f\xe5\x9c\xa8\xe8\x8d\x89\xe4\xb8\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x9a\x90\xe8\x97\x8f\xe5\x9c\xa8\xe8\x8d\x89\xe4\xb8\x9b"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bExcludeSpecialActor"TPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00J\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe3\x00\x00\x00\x02\x00\x00\x00\x92\x00\x00\x00\x06\x00\x00\x00v1\x80\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringR\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/Prefab_Soldier/New_Truck/skill/monster_atk_bullet_noaoe\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00=\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd6\x00\x00\x00\x02\x00\x00\x00\x85\x00\x00\x00\x06\x00\x00\x00v1s\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringE\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/A1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00C\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xdc\x00\x00\x00\x02\x00\x00\x00\x8b\x00\x00\x00\x06\x00\x00\x00v1y\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringK\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/makeDamage\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x9a\x01\x00\x00\x0c\x00\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/common_effects/allhero_jiaxue_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V4\x04\x00\x00\x00\x04\x00\x00\x00>\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd7\x00\x00\x00\x02\x00\x00\x00\x86\x00\x00\x00\x06\x00\x00\x00v1t\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringF\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/526_Summoner/5261_Summoner_LOD1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00<\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd5\x00\x00\x00\x02\x00\x00\x00\x84\x00\x00\x00\x06\x00\x00\x00v1r\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringD\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/526_Summoner/Birth1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00H\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe1\x00\x00\x00\x02\x00\x00\x00\x90\x00\x00\x00\x06\x00\x00\x00v1~\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringP\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/526_Summoner/Summoner_pet_death\x04\x00\x00ram="false"/>\n\t\t\t\t<bool name="bFilterSameCamp" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDiffCamp" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlySelf" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyHostHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bImmediateRevive" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="attackType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x89\x80\xe6\x9c\x89\xe8\x8b\xb1\xe9\x9b\x84"/>\n\t\t\t\t\t<uint name="\xe8\xbf\x91\xe6\x88\x98\xe8\x8b\xb1\xe9\x9b\x84"/>\n\t\t\t\t\t<uint name="\xe8\xbf\x9c\xe7\xa8\x8b\xe8\x8b\xb1\xe9\x9b\x84"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bSelectJob" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="jobType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="N/A"/>\n\t\t\t\t\t<uint name="\xe5\x9d\xa6\xe5\x85\x8b"/>\n\t\t\t\t\t<uint name="\xe6\x88\x98\xe5\xa3\xab"/>\n\t\t\t\t\t<uint name="\xe5\x88\xba\xe5\xae\xa2"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe5\xb8\x88"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x84\xe6\x89\x8b"/>\n\t\t\t\t\t<uint name="\xe8\xbe\x85\xe5\x8a\xa9"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bFilterGrouped" val1_Bright_Show3\x04\x00\x00\x00\x04\x00\x00\x00\xf7\x01\x00\x00\x17\x00\x00\x00ArtLobbyIdleShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xa8\x01\x00\x00\x03\x00\x00\x00\x8c\x00\x00\x00\x0b\x00\x00\x00Elementu\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringG\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_idleShow1\x04\x00\x00\x00\x04\x00\x00\x00\x8c\x00\x00\x00\x0b\x00\x00\x00Elementu\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringG\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_idleShow2\x04\x00\x00\x00\x04\x00\x00\x00\x88\x00\x00\x00\x0b\x00\x00\x00Elementq\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringC\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_Show3\x04\x00\x00\x00\x04\x00\x00\x00\x95\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamerao\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringA\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/540_Bright/5401_Bright_Cam\x04\x00\x00\x00\x04\x00\x00\x00\x0e\x18\x00\x00\x0e\x00\x00\x00SkinPrefabG\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr2\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement[]\x04\x00\x00\x00\xb1\x17\x00\x00\x03\x00\x00\x00\xc2\x07\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00j\x07\x00\x00\x06\x00\x00\x00\xe9\x01\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x9d\x01\x00\x00\x03\x00\x00\x00\x87\x00\x00\x00\x0b\x00\x00\x00Elementp\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringB\x00\x00\x00\x05\x00\x00\x000986.wem\x007\x00\x00\x00\xe2\x00\x00\x00\x03\x00\x00\x00+\x00\x00\x00Sound/Android/Chinese(Taiwan)/97838123.wem\x008\x00\x00\x00\xe3\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/987101814.wem\x008\x00\x00\x00\xe4\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/994406221.wem\x008\x00\x00\x00\xe5\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/995073947.wem\x008\x00\x00\x00\xe6\x00\x00\x00\x03\x00\x00\x00,\x00\x00\x00Sound/Android/Chinese(Taiwan)/995257090.wem\x00$\x00\x00\x00\xe7\x00\x00\x00\x04\x00\x00\x00\x18\x00\x00\x00AssetBundle/Show/BG/*.*\x00E\x00\x00\x00\xe8\x00\x00\x00\x01\x00\x00\x009\x00\x00\x00AssetBundle/Show/Hero/133_DiRenJie_show_base.assetbundle\x00A\x00\x00\x00\xe9\x00\x00\x00\x03\x00\x00\x005\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_DiRenJie_Show.bnk\x00+\x00\x00\x00\xea\x00\x00\x00\x05\x00\x00\x00\x1f\x00\x00\x00AssetBundle/Modules/Soccer/*.*\x00-\x00\x00\x00\xeb\x00\x00\x00\x05\x00\x00\x00!\x00\x00\x00AssetBundle/Modules/FiveCamp/*.*\x00/\x00\x00\x00\xec\x00\x00\x00\x03\x00\x00\x00#\x00\x00\x00Sound/Android/Hero_Zhaoyun_SFX.bnk\x00>\x00\x00\x00\xed\x00\x00\x00\x03\x00\x00\x002\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_Zhaoyun_VO.bnk\x00/\x00\x00\x00\xee\x00\x00\x00\x03\x00\x00\x00#\x00\x00\x00Sound/Android/Hero_XiangYu_SFX.bnk\x00>\x00\x00\x00\xef\x00\x00\x00\x03\x00\x00\x002\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_XiangYu_VO.bnk\x003\x00\x00\x00\xf0\x00\x00\x00\x03\x00\x00\x00\'\x00\x00\x00Sound/Android/Hero_WangZhaoJun_SFX.bnk\x00B\x00\x00\x00\xf1\x00\x00\x00\x03\x00\x00\x006\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_WangZhaoJun_VO.bnk\x00?\x00\x00\x00\xf2\x00\x00\x00\x03\x00\x00\x003\x00\x00\x00Sound/Android/Chinese(Taiwan)/Hero_LiuShan_SFX.bnk\x00>\x00\x00\x00\xf3\x00\x00\x00\x03\x00\x00\x00useRefParam="false"/>\n\t\t\t\t<String name="endClipName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bPlayEndClipName" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ChangeSkillTriggerTick0" eventType="ChangeSkillTriggerTick" guid="7e6b69c3-4a8c-40e5-bbc7-971898233929" enabled="true" useRefParam="false" refParamName="" r="0.800" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="ChangeSkillTriggerTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCurrentSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="slotType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe9\x80\x9a"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd1"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd2"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd3"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd4"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="effectTime" e="\xe4\xb8\x8d\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t\t<uint name="\xe5\xbb\xb6\xe8\xbf\x9f\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t\t<uint name="\xe5\xbc\xba\xe5\x88\xb6\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="interuptAutoAttack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="a66c0c5d-659b-4258-b6f7-6630f5046041" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.117" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="TriggerParticleTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="objectSpaceId" objectName="taMSES\x07\x00\x00\x00}\x00\x00\x00f\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e0a70c7ddff5db1861c7359c802ff1eb\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00y\x00\x00\x00\x01\x00\x00\x00\x01\x01\x14\x00\x00\x00BB2CD71CABB8E0D8_##\x00=\x00\x00\x00UGUI/Particle/UI_MapCircle_effect/UI_MapCircle_effect_Yellow\x00\x14\x00\x00\x008574E33444BD2708_##\x00\x01\x00y\x00\x00\x00\x02\x00\x00\x00\x01\x01\x14\x00\x00\x00033F49AD5A74\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_wukong/wukong_attack_spell02\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00K\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe4\x00\x00\x00\x02\x00\x00\x00\x93\x00\x00\x00\x06\x00\x00\x00v1\x81\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringS\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/167_wukong/wukong_attack_spell02_1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00G\x03\x00\x00\x1d\x00\x00\x00hurtParticlesInFirstLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\xab\x02\x00\x00\x02\x00\x00\x00Q\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xea\x00\x00\x00\x02\x00\x00\x00\x99\x00\x00\x00\x06\x00\x00\x00v1\x87\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringY\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/chusheng_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00R\x01\x00\x00\x0b\x00\x00\x00uncInstant0" eventType="SkillFuncInstant" guid="8d09eb2f-50ed-4358-a741-27ca7e1a94dd" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.000" b="0.667" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillFuncInstant" time="0.000" isDuration="false">\n\t\t\t\t<Enum name="SkillFuncType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe7\x89\xa9\xe7\x90\x86\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe7\x9c\x9f\xe5\xae\x9e\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x94\x9f\xe5\x91\xbd\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ForbidAbilityDuration12" eventType="ForbidAbilityDuration" guid="ae7adc4b-a73f-4229-a4f1-dd860c67f460" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.117" b="0tion" x="0" y="0" z="1500" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bHeroEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseIndicatorDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyDirection" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="modifyDirUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe5\xbd\x93[\xe5\x8f\x82\xe8\x80\x83\xe5\xaf\xb9\xe8\xb1\xa1]\xe6\x9c\x89\xe5\x80\xbc\xe6\x97\xb6\xe4\xb8\x8d\xe4\xbd\xbf\xe7\x94\xa8"/>\n\t\t\t\t\t<uint name="\xe4\xbd\x9c\xe4\xb8\xba\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91\xe5\xae\x83"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<Vector3i name="direction" x="0" y="0" z="0" refParamName="targetdir" useRefParam="true"/>\n\t\t\t\t<bool name="bRotation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="yRotation" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseRecordPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseRecordDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bChangeMaterialWithParent" vaorceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SetCollisionTick" time="0.180" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="bullet" id="2" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="type" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="BOX"/>\n\t\t\t\t\t<uint name="SPHERE"/>\n\t\t\t\t\t<uint name="CYLINDERSECTOR"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bIsBlockMonsterType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockSoliderLine" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockJungleMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockSoliderType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bIsBlockPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="blockCampType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe9\x98\xbb\xe6\x8c\xa1\xe6\x95\x8c\xe5\xaf\xb9\xe9\x98\xb5\xe8\x90\xa5"/>\n\t\t\t\t\t<uint name="\xe9\x98\xbb\xe6\x8c\xa1\xe8\x87\xaa\xe5\xb7\xb1\xe9\x98\xb5\xe8\x90\xa5"22C6_##\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x05\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00e2\x00\x00f2\x00\x00g2\x00\x00h2\x00\x00i2\x00\x00j2\x00\x00k2\x00\x00l2\x00\x00m2\x00\x00n2\x00\x00\xe88\x01\x00\x02\x00\x00\x00x\x05\x00\x00\x14\x05\x00\x00\n\x05\x00\x00\x92\x04\x00\x00\n\x05\x00\x00\x92\x04\x00\x00\x1e\x05\x00\x00\x92\x04\x00\x00x\x05\x00\x00\xe2\x04\x00\x00x\x05\x00\x00\x14\x05\x00\x00\x92\x04\x00\x00x\x05\x00\x00\x05\x00\x00\x00\x97\x04\x00\x00\x82\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00E7CA65090D658757_##\x00\x0e\x00\x00\x00GongBenWuZang\x00\x01\x14\x00\x00\x00C2F5E48F7D5C72F0_##\x00\x07\x00\x00\x00301300\x00L\x00\x00\x00Prefab_Characters/Prefab_Hero/130_GongBenWuZang/130_GongBenWuZang_actorinfo\x00\x01\x00\x00\x00\x01X\x1b\x00\x00\xd7\r\x00\x00=\x00\x00\x00\xaaG\x00\x00\xaa\x00\x00\x00\x00\x00\x00\x00\x89\x00\x00\x00P\x00\x00\x00\xd8\x0e\x00\x00\xc0\xc6-\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\'\x00\x00\xc0\xc6-\x00(\x17\x02\x00\x00\x00\x00\x00`[\x03\x00X\x0f\x02\x00\xd32\x00\x00\x00\x00\x00\x00\xc82\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xd22\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xdc2\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xe62\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x90_\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02\x01\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x04\x00\x00\x00\x06\x00\x00\x00\x08\x00\x00\x00\x06\x00\x00\x00\x02\x03\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x14\x00\x00\x004744E357C306D3C2_##\x00\x01\x11\x00\x00\x00\x19\x00\x00\x00WrapperAI/Hero/HeroLowAI\x00\x1c\x00\x00\x00WrapperAI/Hero/HeroSimpleAI\x00 \x00\x00\x00WrapperAI/Hero/HeroCommonAutoAI\x00 \x00\x00\x00WrapperAI/Hero/HeroCommonAutoAI\x00 \x00\x00\x00WrapperAI/Hero/HeroWarmSimpleAI\x00 \x00\x00\x00WrapperAI/Hero/HeroWarmNormalAI\x00"\x00\x00\x00WrapperAI/Hero/HeroFiveCampSimple\x00\x02\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00BB3239B9CC0563BF_##\x00\x02\x00\x00\x00\x96\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00200065368D0DBAAB_##\x00\x19\x00\x00\x00Play_bobao_gongbenwuzang\x00\x01\x00\x00\x002\x00\x00\x00Prefab_Characters/Prefab_Hero/commonresource/Born\x007\x00\x00\x00PrZ\xf9\xd8O\xb7F\x1bLuaS\x01\x19\x93\r\n\x1a\n\x04\x04\x08\x08xV\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(w@\x01<@Assets/Prefabs/Lua/AOV/MagicLab/MagicLabRewardItemView.lua\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x14\x00\x00\x00\x03\x00@\x00N@\x00\x00\x83\x80@\x00\x93\xc0@\x01\x04\x80\x80\x01C\x00A\x00\x8e@\x01\x00D\x80\x00\x01\x8c\x00\x00\x00\x07\x80\x00\x83\x8c@\x00\x00\x07\x80\x80\x83\x8c\x80\x00\x00\x07\x80\x00\x84\x8c\xc0\x00\x00\x07\x80\x80\x84\x8c\x00\x01\x00\x07\x80\x00\x85\x0b\x00\x00\x01\x0b\x00\x80\x00\x0b\x00\x00\x00\x04\x06Class\x04\x17MagicLabRewardItemView\x04\x02N\x04\x0bCUILuaView\x04\x08require\x04\x19AOV.MagicLab.MagicLabSys\x04\x0edocumentation\x04\rOnViewInited\x04\x08Refresh\x04\nSetCDNPic\x04\nItemClick\x01\x00\x00\x00\x01\x00\x05\x00\x00\x00\x00\x06\x00\x00\x00\r\x00\x00\x00\x01\x00\x02\x17\x00\x00\x00\x0b\x00\x80\x00C@@\x00S\x80\xc0\x00S\xc0\xc0\x00S\x00\xc1\x00S@\xc1\x00\x07@\x00\x80C@@\x00S\x80\xc0\x00S\xc0\xc0\x00S\x00\xc1\x00S\xc0\xc1\x00\x07@\x00\x83C@@\x00S@\xc2\x00\x07@\x00\x84C@@\x00S\x80\xc0\x00S\xc0\xc0\x00S\x00\xc1\x00S\xc0\xc2\x00\x07@\x00\x85\x0b\x00\x80\x00\x0c\x00\x00\x00\x04\x0cListElement\x04\x03CS\x04\x07Assets\x04\x08Scripts\x04\x03UI\x04\x15CUIListElementScript\x04\x07CDNpic\x04\x10CDNPicComponent\x04\x08BoxText\x04\x06Text2\x04\x0bClickEvent\x04\x0fCUIEventScript\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x17\x00\x00\x00\x08\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\t\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\n\x00\x00\x00\x0b\x00\x00\x00\x0b\x00\x00\x00\x0b\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\x0c\x00\x00\x00\r\x00\x00\x00\x01\x00\x00\x00\x05self\x00\x00\x00\x00\x17\x00\x00\x00\x01\x00\x00\x00\x05_ENV\x00\x0f\x00\x00\x00\x17\x00\x00\x00\x01\x00\x05\r\x00\x00\x00\x07@@\x80S\x80@\x00\x8c\x00\x00\x00G\x80\x80\x81S\x00A\x00l@\xc1\x00\xc3\x80A\x00\x03\xc1A\x00\x13\x01B\x02\xc4\x00\x00\x01D\x80\x00\x00G\x80\xc2\x84\x0b\x00\x80\x00\x0b\x00\x00\x00\x04\x06BoxID\x13\xff\xff\xff\xff\xff\xff\xff\xff\x04\x0bClickEvent\x04\x08onClick\x04\x0cListElement\x04\rGetComponent\x04\x07typeof\x04\x02N\x04\x0fCUIEventScript\x04\x08enabled\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x12\x00\x00\x00\x14\x00\x00\x00\x00\x00\x02\x04\x00\x00\x00\x05\x00\x00\x00,\x00@\x00\x04@\x00\x01\x0b\x00\x80\x00\x01\x00\x00\x00\x04\nItemClick\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x04\x00\x00\x00\x13\x00\x00\x00\x13\x00\x00\x00\x13\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x05self\r\x00\x00\x00\x10\x00\x00\x00\x12\x00\x00\x00\x14\x00\x00\x00\x14\x00\x00\x00\x16\x00\x00\x00\x16\x00\x00\x00name="_TargetPos" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t</RefParamList>\n\t<Action tag="" length="1.000" loop="false">\n\t\t<Track trackName="SpawnBulletTick0" eventType="SpawnBulletTick" guid="6c8555eb-3d65-40dc-b96b-22085a7b349f" enabled="true" refParamName="" useRefParam="false" r="1.000" g="0.000" b="0.MSES\x07\x00\x00\x00\x18\x00\x00\x00\t\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00f36f7a0cf63b751b43487af3ac37a561\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00\x01\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00HB\x00\x00\xc8B\x14\x00\x00\x00\x05\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0A\x00\x00HB\x14\x00\x00\x00\n\x00\x00\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00 A\x00\x00\xf0A\x14\x00\x00\x00\x14\x00\x00\x002\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0@\x00\x00 A\x14\x00\x00\x002\x00\x00\x00d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x00\x00\xa0@\x14\x00\x00\x00d\x00\x00\x00\xf4\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80?\x14\x00\x00\x00\xf4\x01\x00\x00\xe8\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xcd\xcc\xcc=\x14\x00\x00\x00\xe8\x03\x00\x00\x88\x13\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\xd7\xa3=\x14\x00\x00\x00\x88\x13\x00\x00\x10\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xcd\xccL=MSES\x07\x00\x00\x00^\x00\x00\x00\x06\x01\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00ea39319bc554c025c5f107f401c732b8\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00L\x00\x00\x00e\x00\x00\x00\x14\x00\x00\x00C235D3F892E815B5_##\x00\x14\x00\x00\x006E67E299EE10381A_##\x00\n\x00\x00\x00touxiang1\x00\x01\x01\x01\x00\x00\x00\x00\x00\x01\x01L\x00\x00\x00f\x00\x00\x00\x14\x00\x00\x008BD1A0FD4DFCA919_##\x00\x14\x00\x00\x005696820E83B5B08F_##\x00\n\x00\x00\x00touxiang2\x00\x01\x01\x01\x00\x00\x00\x00\x00\x01\x01L\x00\x00\x00g\x00\x00\x00\x14\x00\x00\x007B989B6E5EDFA305_##\x00\x14\x00\x00\x00498F4E0296"" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterHeroPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDeadControlHero" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterCurrentTarget" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMoveDirection" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Angle" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyOneKillActor" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyBigMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyMe" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="bulletID" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterCantAttack" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterSpecialType1" valu\x00\x00\x00\x04\x00\x00\x00\x91\x00\x00\x00\x0b\x00\x00\x00Elementz\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringL\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/153_LanLingWang/1533_LanLingWang_LOD3\x04\x00\x00\x00\x04\x00\x00\x007\x01\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xe8\x00\x00\x00\x02\x00\x00\x00\x92\x00\x00\x00\x0b\x00\x00\x00Element{\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringM\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/153_LanLingWang/1533_LanLingWang_Show1\x04\x00\x00\x00\x04\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00]\x00\x00\x00\x1a\x00\x00\x00ArtSkinLobbyShowCamera7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00R\x00\x00\x00\x0f\x00\x00\x00SavedSkinId7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V0\x04\x00\x00\x00\x04\x00\x00\x00W\x00\x00\x00\x11\x00\x00\x00CrossFadeTime:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Single\x0c\x00\x00\x00\x05\x00\x00\x00V0.3\x04\x00\x00\x00\x04\x00\x00\x00#\x04\x00\x00\x10\x00\x00\x00TransConfigsK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig[]\x04\x00\x00\x00\xc0\x03\x00\x00\x02\x00\x00\x00\xda\x01\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00~\x01\x00\x00\x02\x00\x00\x00)\x01\x00\x00\n\x00\x00\x00Offset4\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x1f\x00\x00\x00\x08\x00\x00\x00TypeUnityEngine.Vector3\x04\x00\x00\x00\xe3\x00\x00\x00\x03\x00\x00\x00I\x00\x00\x00\x05\x00\x00\x00x8\x00\x00\x00\x03 r="0.100" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="3" guid="09805859-49f5-4ed0-8a41-b9b2b75ce864" status="true"/>\n\t\t\t<Event eventName="StopTrack" time="0.000" isDuration="false">\n\t\t\t\t<TrackObject name="trackId" id="0" guid="c890e4ed-8300-4e21-8d66-757283ec3cc0" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="StopTrack5" eventType="StopTrack" guid="b3cfc329-c442-4487-ab73-1d5ffcf3a8d7" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.133" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="3" guid="09805859-49f5-4ed0-8a41-b9b2b75ce864" status="true"/>\n\t\t\t<Event eventName="StopTrack" time="0.000" isDuration="false">\n\t\t\t\t<TrackObject name="trackId" id="2" guid="d1939f1f-84aa-46f2-9322-abcc2231ad1a" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x120X\xbc\xa5S\x00\x00\xa5S\x00\x00#\x00\x00\x00196_Elsu/skill/AfterLastEvent="true">\n\t\t\t<Event eventName="HitTriggerTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="hitTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInheritRefParams" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="triggerId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bulletHit" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="victimId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="lastHit" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSkillCombineChoose" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_1" value="1841001" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SelfSkillCombineID_2" val\t<Vector3i name="offsetDir" x="0" y="0" z="0" refParamName="_TargetDir" useRefParam="true"/>\n\t\t\t\t<Enum name="hitPoint" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe8\x83\xb8\xe9\x83\xa8"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xb4\xe9\x83\xa8"/>\n\t\t\t\t</Enum>\n\t\t\t\t<Enum name="MoveType" value="2" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe7\x9b\xae\xe6\xa0\x87"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe4\xbd\x8d\xe7\xbd\xae"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x87\xe5\xae\x9a\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="distance" value="5000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="velocity" value="18000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="gravity" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bMoveRotate" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAdjustSpeed" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration0" eventType="HitTriggerDuration" guid="1e0b1d40-f329-4718-b4d0-d5c0caaaa1e4" enabled="true" lod="0" useRefParam="false" refParamName="" r="1.000" g="0.233" b="me="checkNoMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenEntering" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenLeaving" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="PlayAnimDuration0" eventType="PlayAnimDuration" guid="9d243092-f160-4189-a9da-f132595032c9" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.650" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="PlayAnimDuration" time="0.000" length="1.267" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="clipName" value="Atk1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDontReplaceSameAnim" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="layer" value="1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="subLayer" .Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00I\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe2\x00\x00\x00\x02\x00\x00\x00\x91\x00\x00\x00\x06\x00\x00\x00v1\x7f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringQ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/AutoChess/acA1E1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00O\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xe8\x00\x00\x00\x02\x00\x00\x00\x97\x00\x00\x00\x06\x00\x00\x00v1\x85\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringW\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/New_MeleeSoldier/skill/AutoChess/acmakeDamage\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x9b\x01\x00\x00\x0c\x00\x00\x00skillIDsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x10\x01\x00\x00\x01\x00\x00\x00\x08\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\xa1\x00\x00\x00\x02\x00\x00\x00P\x00\x00\x00\x06\x00\x00\x00v1>\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x10\x00\x00\x00\x05\x00\x00\x00V6710002\x04\x00\x00\x00\x04\x004_##\x00>\x00\x00\x00\x1e\x00\x00\x00\t\x00\x00\x00\x00<\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":63}]}\x00\n\x00\x00\x00y\x00\x00\x00\x02\x00\x00\x00\xd0\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x002B5B6A1F7A9007E5_##\x00?\x00\x00\x00$\x00\x00\x00\t\x00\x00\x00\x00<\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":63}]}\x00\n\x00\x00\x00>\x00\x00\x00\x02\x00\x00\x00\xd1\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00EE2974C205C472E7_##\x00\x01\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x01\x01\x00\x00\x00\x00\n\x00\x00\x00y\x00\x00\x00\x02\x00\x00\x00\xd2\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x002521BBD3EE0BDF80_##\x00<\x00\x00\x00\x06\x00\x00\x00\x01\x00\x00\x00\x01<\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":68}]}\x00\n\x00\x00\x00>\x00\x00\x00\x02\x00\x00\x00\xd3\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00BDB77D73EF3CDFB6_##\x00\x03\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x01\x01\x00\x00\x00\x00\n\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd4\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x00898A75C147D555B3_##\x00\x06\x00\x00\x00\n\x00\x00\x00\x02\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00\n\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd5\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x14\x00\x00\x00FA3AF0603BDD9365_##\x00\x07\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00x\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd6\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x0051ED5D030B64764D_##\x00\n\x00\x00\x00\t\x00\x00\x00\x03\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00\n\x00\x00\x00x\x00\x00\x00\x02\x00\x00\x00\xd7\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x14\x00\x00\x00C50583CB6167E4E5_##\x00\x0b\x00\x00\x00\x05\x00\x00\x00\x03\x00\x00\x00\x00;\x00\x00\x00{"ContentUrl":"","actions":[{"name":"OpenForm","Form":5}]}\x00x\x00\x00\x00y\x00\x00\x00\x02\x00\x00\x00\xd8\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x14\x00\x00\x004721F4D35F33FCA5_##\x00\x0c\x00\x00\x00\x08\x00\x00\x00\x02\x00\x00\x00\x00<\x00\x00\xe6\x9c\xaf\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe5\xbc\xba\xe5\xba\xa6\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe5\xa2\x9e\xe7\x9b\x8a\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe8\x84\xb1\xe7\xa6\xbb\xe6\x88\x98\xe6\x96\x97\xe6\x8f\x90\xe9\x80\x9f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x9b\xbe\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x94\xb2\xe5\x87\x8f\xe4\xbc\xa4\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe7\x94\x9f\xe5\x91\xbd\xe4\xbd\x8e\xe6\x97\xb6\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe8\x87\xb4\xe7\x9b\xb2"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe9\x99\xa4\xe6\x8a\x80\xe8\x83\xbd\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe9\x87\x91\xe5\xb8\x81\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd\xe9\xa2\x9d\xe5\xa4\x96\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe8\xa2\xab\xe5\x8a\xa8\xe6\x8a\x80\xe8\x83\xbd\xe5\x8f\x82\xe6\x95\xb0"/>\n\t\t\t\t\t<uint name="\xe6\x94\xb9\xe5\x8f\x98\xe7\x8b\x82\xe6\x84\x8f\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe7\x8e\xb0\xe5\xbd\xa2\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>\n\nPK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00HF\xa6,D\x0e\x00\x00D\x0e\x00\x00+\x00\x00\x00177_ChengJiSiHan/skill/AutoChess/acA1E3.xml<?xml version="1.0" encoding="utf-8"?>\n<Project>\n\t<TemplateObjectList>\n\t\t<TemplateObject objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false"/>\n\t\t<TemplateObject objectName="target" id="1" isTemp="false"/>\n\t</TemplateObjectList>\n\t<RefParamList/>\n\t<Action tag="" length="0.300" loop="false">\n\t\t<Track trackName="SkillFuncDuratio-9322-abcc2231ad1a" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="0.833" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="TriggerParticle" time="0.000" length="1.100" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="bullet1" id="3" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="objectSpaceId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<uint name="RefLiteBulletID" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="parentResourceName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName" value="prefab_skill_effects/hero_skill_effects/174_yuji/yuji_attack01_spell02" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName2" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName3" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="dontShowIfNoBindPoint" valtem.Int32]\x04\x00\x00\x00\xeb\x00\x00\x00\x02\x00\x00\x00\x9a\x00\x00\x00\x06\x00\x00\x00v1\x88\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringZ\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/huijidi_dead\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00S\x0e\x00\x00\x19\x00\x00\x00particlesInOtherLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\xbb\r\x00\x00\x0b\x00\x00\x00\x1f\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xb8\x00\x00\x00\x02\x00\x00\x00f\x00\x00\x00\x06\x00\x00\x00v1T\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String&\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/commonempty\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x06\x00\x00\x00v28\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0b\x00\x00\x00\x05\x00\x00\x00V10\x04\x00\x00\x00\x04\x00\x00\x00@\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd9\x00\x00\x00\x02\x00\x00\x00\x88\x00\x00\x00\x06\x00\x00\x00v1v\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringH\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/hero_skill_effects/109_daji/daji_attack_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V3\x04\x00\x00\x00\x04\x00\x00\x00A\x01\x00\x00\x0b\x00\x00\x00\n\t\t\t\t<bool name="forbidEnergyRecover" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="MoveIgnoreObstructArea" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidCollisionDetection" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="ImmuneSkillSelect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReplaceHPBarImmuneSelect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidCallBoss" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidExtraBtnSlot1" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillInputCacheDuration0" eventType="SkillInputCacheDuration" guid="43618e12-f288-4877-9d44-4cb1ef89f0a2" enabled="true" useRefParam="false" refParamName="" r="0.467" g="1.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillInputCacheDuration" time="0.000" length="0.333" isDur1200\x04\x00\x00\x00\x04\x00\x00\x00t\x00\x00\x00\x12\x00\x00\x00BtResourcePathV\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String(\x00\x00\x00\x05\x00\x00\x00VWrapperAI/Hero/HeroCommonAutoAI\x04\x00\x00\x00\x04\x00\x00\x00\x85\x00\x00\x00\x0f\x00\x00\x00deadAgePathj\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String<\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/536_Ninja/skill/Death\x04\x00\x00\x00\x04\x00\x00\x00PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA\x00\x00\x00\x00Prefab_Hero/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\xedA*\x00\x00\x00Prefab_Hero/544_Painter/PK\x01\x02\x1e\x03\n\x00\x00\x00\x00\x00\x00\x00!\x00\xc5z\x03\xef/\x0c\x00\x00/\x0c\x00\x003\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81`\x00\x00\x00Prefab_Hero/544_Painter/544_Painter_actorinfo.bytesPK\x05\x06\x00\x00\x00\x00\x03\x00\x03\x00\xe1\x00\x00\x00\xe0\x0c\x00\x00\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00Prefab_Hero/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1a\x00\x00\x00Prefab_Hero/148_JiangZiYa/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00h-\x11\x99U\x1f\x00\x00U\x1f\x00\x007\x00\x00\x00Prefab_Hero/148_JiangZiYa/148_JiangZiYa_actorinfo.bytesU\x1f\x00\x00\x08\x00\x00\x00ROOTD\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom/\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.CActorInfo\x04\x00\x00\x00\x01\x1f\x00\x00\x0f\x00\x00\x00]\x00\x00\x00\r\x00\x00\x00ActorNameD\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\x16\x00\x00\x00\x05\x00\x00\x00V148_JiangZiYa\x04\x00\x00\x00\x04\x00\x00\x00\xf7\x01\x00\x00\x10\x00\x00\x00ArtPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xaf\x01\x00\x00\x03\x00\x00\x00\x8d\x00\x00\x00\x0b\x00\x00\x00Elementv\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringH\x00\x00\x00\x05\x00\x00>\n\t\t\t\t<bool name="bUseTargetSkinEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bReplayWhenChangeMesh" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTrailProtect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bKeepChildScale" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="extend" value="10" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="particleScaleGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableMaxFollowTime" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="maxFollowTime" value="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bindOnHUD" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="showInStatus" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xbb\xbb\xe6\x84\x8f\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="Idle\xe7\x8a\xb6\xe6\x80\x81"/>\n\t\t\t\t\t<uint name="\xe7\xa7\xbb\xe5\x8a\xa8\xe7\x8a\xb6\xe6\x80\x81"\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x001\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xca\x00\x00\x00\x02\x00\x00\x00y\x00\x00\x00\x06\x00\x00\x00v1g\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String9\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/New_Common_Effects/HeroStun\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x008\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd1\x00\x00\x00\x02\x00\x00\x00\x80\x00\x00\x00\x06\x00\x00\x00v1n\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String@\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/New_Common_Effects/Dragon_Buff_red\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x004\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcd\x00\x00\x00\x02\x00\x00\x00|\x00\x00\x00\x06\x00\x00\x00v1j\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String<\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/New_Common_Effects/Dragon_Buff\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xbc\x07\x00\x00\x0e\x00\x00\x00animationsw\x00\t\t<String name="SpecialActionName" value="prefab_characters/prefab_hero/115_gaojianli/skill/a1b2" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDeadRemove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bImmeExcute" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAgeEternal" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="bulletTypeId" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="bulletUpperLimit" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSpawnBounceBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="bulletSkillType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe9\xbb\x98\xe8\xae\xa4\xe7\xb1\xbb\xe5\x9e\x8b_0"/>\n\t\t\t\t\t<uint name="\xe5\x85\x81\xe8\xae\xb8\xe7\x89\xb9\xe6\xae\x8a\xe6\x89\x93\xe6\x96\xad_1"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDestroyedBySpecialBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="ChangeSkillTrigger\t\t\t\t<bool name="forbidFilterSkill4" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill5" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill6" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill7" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill8" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill9" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill10" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill11" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSummonerSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterMapSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterEquipActiveSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterActiveSame="bLayOnNavMesh" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRealTimeSight" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOpenSight" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEnableAnimation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBlockObj" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkin" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRecordObjPosition" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="recordTargeID" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyFollowPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TrackObject name="trackId" id="-1" guid="00000000-0000-0000-0000-000000000000" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SetCollisionTick0" eventType="SetCollisionTick" guid="dcd824ef-bb03-4fc8-bf5c-a64a29c3c0\t<int name="ExternalRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="InnerRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="InnerRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Rotation" value="160" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="HeightGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="RotationGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t</EMSES\x07\x00\x00\x00\x1c\x00\x00\x00\x0e\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x009b0dbb76c4f9d3da6c78991155e5e1c2\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x03\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x05\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x06\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x07\x00\x00\x00\x02\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\t\x00\x00\x00\x02\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\n\x00\x00\x00\x02\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\n\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x0b\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x0c\x00\x00\x00\x03\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\r\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x18\x00\x00\x00\x0e\x00\x00\x00\x03\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x91\xb0\x00\x00\x08\x00\x00\x00RargetSkillCombine_2" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="TargetSkillLeaveRemove_2" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TargetSkillCombine_3" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="TargetSkillLeaveRemove_3" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTriggerBullet" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="BulletActionName" value="prefab_characters/prefab_hero/141_diaochan/skill/extend/exs2b1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAgeImmeExcute" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseTriggerObj" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForceUseTriggerObj" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCheckSight" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTriggerMode" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bTriggerBounceBullete"/>\n\t\t\t\t<int name="triggerInterval" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TriggerActorInterval" value="30" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterEnemy" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterFriend" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFileterMonter" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterChest" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFileterOrgan" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterEye" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMyself" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterDead" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterHeroPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyOneKillActor" \xe5\x87\x8f\xe5\xb0\x91\xe6\xb3\x95\xe6\x9c\xaf\xe7\xa9\xbf\xe9\x80\x8f"/>\n\t\t\t\t\t<uint name="\xe6\x8a\xa4\xe7\x9b\xbe"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x8a\x80\xe8\x83\xbd\xe5\x8d\xb0\xe8\xae\xb0"/>\n\t\t\t\t\t<uint name="\xe8\xa7\xa6\xe5\x8f\x91\xe6\x8a\x80\xe8\x83\xbd\xe5\x8d\xb0\xe8\xae\xb0"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x8e\xa7\xe5\x88\xb6"/>\n\t\t\t\t\t<uint name="\xe8\xbf\x85\xe9\x80\x9f\xe5\xa4\x8d\xe6\xb4\xbb"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe7\x90\x83\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\xa9\xb1\xe6\x95\xa3\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe7\x89\xa9\xe7\x90\x86\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe5\x85\x8d\xe7\x96\xab\xe7\x8e\x87"/>\n\t\t\t\t\t<uint name="\xe8\x8e\xb7\xe5\x8f\x96\xe8\xa7\x86\xe9\x87\x8e\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x9a\x90\xe8\xba\xab\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe4\xbc\xa4\xe5\xae\xb3\xe8\xbe\x93\xe5\x87\xba\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x9f\xa7\xe6\x80\xa7\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x86\xb7\xe5\x8d\xb4\xe7\xbc\xa9\xe5\x87\x8f\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x97\xe6\x9a\xb4\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x9d\xa1\xe4\xbb\xb6\xe4\xbc\xa4\xe5\xae\xb3\xe8\xbe\x93\xe5\x87\xba\xe7\x8e\x87\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xbf\xbd\xe7\x95\xa5RVO"/>\n\t\t\t\t\t<uint name="\xe7\x94\x9f\xe5\x91\xbd\xe6\x9d\xa1\xe4\xbb\xb6\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe6\x9b\xb4\xe6\x8d\xa2\xe8\xa1\x80\xe6\x9d\xa1\xe9\xa3\x8e\xe6\xa0\xbc"/>\n\t\t\t\t\t<uint name="\xe7\x9b\xae\xe6\xa0\x87\xe4\xbc\xa4\xe5\xae\xb3\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe7\xbb\x8f\xe9\xaa\x8c\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xbb\x8f\xe9\xaa\x8c\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x8f\x97\xe6\x8e\xa7\xe9\xa2\x9d\xe5\xa4\x96\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe5\x85\x8d\xe7\x96\xab\xe6\x9a\xb4\xe5\x87\xbb\xe6\x95\x88\xe6\x9e\x9c"/>\n\t\t\t\t\t<uint name="\xe9\x99\x90\xe5\x88\xb6\xe6\x9c\x80\xe5\xa4\xa7\xe4\xbc\xa4\xe5\xae\xb3\xe6\x95\x88\xe6\x9e\x9c"<int name="level3Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="level4Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="level5Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="level6Id" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOtherSkillAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillUseCacheTick0" eventType="SkillUseCacheTick" guid="53c33571-7838-484f-9f06-7b93d4bc28e0" enabled="true" useRefParam="false" refParamName="" r="0.000" g="1.000" b="0.217" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillUseCacheTick" time="0.350" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SpawnObjectDuration0" eventType="SpawnObjectDuration" guid="e8a22af8-4078-4313-893b-f729c0f328ed" enabled="false" useRalse"/>\n\t\t\t\t<bool name="bUseRealScaling" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEnableOptCull" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseHeroLocalForward" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="lookTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBulletDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bBullerPosDir" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyFollowPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotateFollowCamera" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRandomRotation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<EulerAngle name="randRotBegin" x="0.ramName="" useRefParam="false"/>\n\t\t\t\t<int name="changeSkillID4Probability" value="100" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="recoverSkillID" value="612800" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCheckCondition" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOvertimeCD" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSendEvent" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="attackTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="refSkillSlot" value="1" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe6\x94\xbb"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd1"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd2"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd3"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd4"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa9\xe8\xb5\x8b\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e"/>\n\t\t\t\t\t<uint name="\xe9\xa5\xb0\xe5\x93\x81\xe6\xa0\x8f\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="level0Id" valuname="\xe9\x98\xbb\xe6\x8c\xa1\xe6\x89\x80\xe6\x9c\x89\xe9\x98\xb5\xe8\x90\xa5"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bVaildBlockForSelfTeamHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bVaildBlockForEnemyTeamHero" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="Pos" x="0" y="0" z="-1000" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="Size" x="2000" y="10000" z="3000" refParamName="" useRefParam="false"/>\n\t\t\t\t<Array name="PosList" refParamName="" useRefParam="false" type="Vector3i"/>\n\t\t\t\t<int name="Radius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorRadius" value="1000" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Height" value="500" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorExternalRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorInnerRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="SectorInnerRadiusGrowthValue" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="Degree" value="160" refP\x00\x00\x00\x02\x00\x00\x00\x7f\x00\x00\x00\x06\x00\x00\x00v1m\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String?\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/commonresource/Dead_Born\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x003\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcc\x00\x00\x00\x02\x00\x00\x00{\x00\x00\x00\x06\x00\x00\x00v1i\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String;\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/538_Iggy/skill/Death\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x000\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xc9\x00\x00\x00\x02\x00\x00\x00x\x00\x00\x00\x06\x00\x00\x00v1f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String8\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/538_Iggy/skill/A1\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x002\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcb\x00\x00\x00\x02\x00\x00\x00z\x00\x00\x00\x06\x00\x00\x00v1h\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String:\x00\x00\x00\x05\x00\x00\x00Vprefab_characters/prefab_hero/\x00h\x00\x00\x00\x01\x00\x00\x00`\x00\x00\x00\x0b\x00\x00\x00ElementI\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom4\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.TransformConfig\x04\x00\x00\x00\x04\x00\x00\x00k\x00\x00\x00\x14\x00\x00\x00SpecialFadeTimesK\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr6\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SpeicalFadeTime[]\x04\x00\x00\x00\x04\x00\x00\x00S\x00\x00\x00\r\x00\x00\x00hudHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V2200\x04\x00\x00\x00\x04\x00\x00\x00g\x00\x00\x00\x0b\x00\x00\x00HudTypeP\x00\x00\x00\x03\x00\x00\x00\x0e\x00\x00\x00\x06\x00\x00\x00JTEnum0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.HudCompType\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00n\x00\x00\x00\x11\x00\x00\x00collisionTypeQ\x00\x00\x00\x03\x00\x00\x00\x0e\x00\x00\x00\x06\x00\x00\x00JTEnum1\x00\x00\x00\x08\x00\x00\x00TypeNucleusDrive.Share.CollisionShapeType\n\x00\x00\x00\x05\x00\x00\x00V2\x04\x00\x00\x00\x04\x00\x00\x00$\x01\x00\x00\x14\x00\x00\x00iCollisionCenter&\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom\x11\x00\x00\x00\x08\x00\x00\x00TypeVInt3\x04\x00\x00\x00\xe2\x00\x00\x00\x03\x00\x00\x00H\x00\x00\x00\x05\x00\x00\x00x7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V0\x04\x00\x00\x00\x04\x00\x00\x00J\x00\x00\x00\x05\x00\x00\x00y9\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\x0c\x00\x00\x00\x05\x00\x00\x00V200\x04\x00\x00\x00\x04\x00\x00\x00H\x00\x00\x00\x05\x00\x00\x00z7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V0\x04\x00\x00\x00\x04\x00\x00\x00W\x00\x00\x00\x11\x00\x00\x00iBulletHeight:\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\r\x00\x00\x00\x05\x00\x00\x00V1600\x04\x00\x00\x00\x04\x00\x00\x00v\x00\x00\x00\x12\x00\x00\x00BtResourcePathX\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String*\x00\x00\x00\x05\x00\x00\x00VWrapperAI/Soldier/BTSoldierNormal\x04\x00\x00\x00\x04\x00\x00\x00\x8d\x00\x00\x00\x0f\x00\x00\x00deadAgePathramName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterSpecialType2" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyBeControledActor" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyAttackerPet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyDeadOrgan" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterCanntAttackOrgan" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="TriggerActorCount" value="32" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="SelectMode" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe9\x9a\x8f\xe6\x9c\xba\xe9\x80\x89\xe6\x8b\xa9"/>\n\t\t\t\t\t<uint name="\xe8\xa1\x80\xe9\x87\x8f\xe9\x80\x89\xe6\x8b\xa9"/>\n\t\t\t\t\t<uint name="\xe6\x8c\x89\xe7\x9c\xbc\xe7\x9a\x84\xe8\xa7\x84\xe5\x88\x99\xe9\x80\x89\xe6\x8b\xa9"/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="CollideMaxCount" value="1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxTriggerCount" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="MaxSelfBuffCount" am="false" />\r\n        <bool name="bExtraBuff" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bOverrideParam" value="false" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam1" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam2" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam3" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam4" value="0" refParamName="" useRefParam="false" />\r\n        <int name="buffOverrideParam5" value="0" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="paramTargetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false" />\r\n        <TemplateObject name="paramTargetId2" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false" />\r\n      </Event>\r\n    </Track>\r\n    <Track trackName="StopTrack1" eventType="StopTrack" guid="4ce273d3-51d6-4fe0-8fbe-1ff46fefa576" enabl guid="884649fb-eee1-4f09-8e8c-136817834eb9" enabled="true" useRefParam="false" refParamName="" r="0.900" g="0.000" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SetBehaviourModeTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="stopMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="stopCurSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="delayStopCurSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="deadControl" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SetAttackDirDuration0" eventType="SetAttackDirDuration" guid="13f98c0c-0c95-4e18-aeb2-1fef43e76e8b" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.333" b="0="SkillInputCacheDuration" time="0.233" length="0.100" isDuration="true">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cacheSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceCacheSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCacheSkillReCalcLock" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="cacheMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceCacheMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="checkMoveAbortCurSkill" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="checkNoMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenEntering" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="clearCacheMoveWhenLeaving" value="false" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="PlayAnimDure"/>\n\t\t\t\t<int name="animatorOverrideLayer" value="-1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bLoop" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="crossFadeTime" value="0.100" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseFadeOutTime" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="fadeOutTime" value="0.200" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="startTime" value="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="endTime" value="99999.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeed" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="alwaysAnimate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bKeepOldSpeed" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bCanNotBeCulled" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="beginClipName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bPlayBeginCliTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringK\x00\x00\x00\x05\x00\x00\x00Vprefab_skill_effects/tongyong_effects/tongyong_hurt/fireta_hurt_01\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00MSES\x07\x00\x00\x00 \x00\x00\x00\x04\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00825732d46fb1b030cdac35cc22c3f23d\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x00\x00\x07\x00\x00\x00\x14\x00\x00\x00A409CCAC72376898_##\x00\x1c\x00\x00\x00\x1e\x00\x00\x00\x14\x00\x00\x000629BC043F5D2625_##\x00\x1c\x00\x00\x00d\x00\x00\x00\x14\x00\x00\x007D56267D87A29EDD_##\x00\x1c\x00\x00\x00m\x01\x00\x00\x14\x00\x00\x00DFB6F47F471FD135_##\x00\x13\x0f\x00\x00\x08\x00\x00\x00ROOTC\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom.\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.AssetReferenceSet\x04\x00\x00\x00\xc0\x0e\x00\x00\x01\x00\x00\x00\xb8\x0e\x00\x00\x0e\x00\x00\x00baseSubsetF\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom1\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.AssetReferenceSubset\x04\x00\x00\x00\\\x0e\x00\x00\x04\x00\x00\x00l\x05\x00\x00\x0b\x00\x00\x00actionsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00\xe2\x04\x00\x00\x04\x00\x00\x005\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xce\x00\x00\x00\x02\x00\x00\x00}\x00\x00\x00\x06\x00\x00\x00v1k\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String=\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Soldier/Soldier1/skill/M1A1\x04\x00\x00\x00\x04\x00>\n\t\t\t\t<bool name="bTargetPosition" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="targetPosition" x="0" y="0" z="0" refParamName="" useRefParam="true"/>\n\t\t\t\t<String name="prefabName" value="prefab_characters/commonempty" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bMoveCollision" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="recreateExisting" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="superTranslation" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyTranslation" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3i name="translation" x="-600" y="1400" z="500" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="modifyDirection" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="modifyDirUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe5\xbd\x93[\xe5\x8f\x82\xe8\x80\x83\xe5\xaf\xb9\xe8\xb1\xa1]\xe6\x9c\x89\xe5\x80\xbc\xe6\x97\xb6\xe4\xb8\x8d\xe4\xbd\xbf\xe7\x94\xa8"/>\n\t\t\t\t\t<uint name="\xe4\xbd\x9c\xe4\xb8\xba\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91"/>\n\t\t\t\t\t<uint name="\xe6\x9c\xac\xe7\x89\xa9\xe4\xbd\x93\xe6\x9c\x9d\xe5\x90\x91\xe5\xae\x83"/>\n\t\t="" useRefParam="false"/>\n\t\t\t\t<int name="layer" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="enableTag" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="tag" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToAnimation" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="sightRadius" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bSameVisibleAsAttacker" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseSkinAdvance" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="visionActorId" objectName="\xe6\x94\xbb\xe5\x87\xbb\xe8\x80\x85" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bVisibleByFow" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bInvisibleBullet" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bForbidBulletInObstacle" va\t\t<uint name="\xe6\xb3\x95\xe6\x9c\xaf\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe7\x9c\x9f\xe5\xae\x9e\xe4\xbc\xa4\xe5\xae\xb3"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\xa4\x8d\xe7\x94\x9f\xe5\x91\xbd\xe5\x80\xbc"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe6\x94\xbb\xe5\x87\xbb\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\xa2\x9e\xe5\x8a\xa0\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe5\x87\x8f\xe5\xb0\x91\xe7\xa7\xbb\xe5\x8a\xa8\xe9\x80\x9f\xe5\xba\xa6"/>\n\t\t\t\t\t<uint name="\xe6\x8f\x90\xe9\xab\x98\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe9\x99\x8d\xe4\xbd\x8e\xe6\x94\xbb\xe5\x87\xbb\xe5\x8a\x9b"/>\n\t\t\t\t\t<uint name="\xe5\x90\xb8\xe8\xa1\x80"/>\n\t\t\t\t</Enum>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="TriggerParticleTick0" eventType="TriggerParticleTick" guid="c41c436a-6fd5-4207-a69b-f3ffebeadf55" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.583" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="TriggerParticleTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="objectSpaceId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bDonotAttackToMesh" valuSoundTick7" eventType="PlayHeroSoundTick" guid="a23129b2-cb41-44f8-93ff-cf6c2ceaf519" enabled="true" refParamName="" useRefParam="false" r="0.000" g="1.000" b="1.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="PlayHeroSoundTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<TemplateObject name="sourceId" objectName="None" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="eventName" value="Play_Meilin_Wanou_Skill_Hit_1" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="use1P3PSwitch" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="useSkinSwitch" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<Array name="extraSkinId" refParamName="" useRefParam="false" type="uint"/>\n\t\t\t</Event>\n\t\t</Track>\n\t</Action>\n</Project>\n\nPK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\xffZ\x87\xc0\xeaa\x00\x00\xeaa\x00\x00*\x00\x00\x00Prefab_Monster/137_SiMaYi_Pet/skill/A2.xml<?xLLY\x04\x00\x00\x00\x04\x00\x00\x00,\x00\x00\x00\x0b\x00\x00\x00Element\x15\x00\x00\x00\x01\x00\x00\x00\r\x00\x00\x00\x08\x00\x00\x00NULLY\x04\x00\x00\x00\x04\x00\x00\x00V\x00\x00\x00\x1a\x00\x00\x00PreloadAnimatorEffects0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\x04\x00\x00\x00A\x06\x00\x00\x0b\x00\x00\x00ElementE\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom0\x00\x00\x00\x08\x00\x00\x00TypeAssets.Scripts.GameLogic.SkinElement\x04\x00\x00\x00\xe9\x05\x00\x00\x05\x00\x00\x00\x01\x02\x00\x00\x14\x00\x00\x00ArtSkinPrefabLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xb5\x01\x00\x00\x03\x00\x00\x00\x8f\x00\x00\x00\x0b\x00\x00\x00Elementx\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/506_DarkKnight/5067_DarkKnight_LOD1\x04\x00\x00\x00\x04\x00\x00\x00\x8f\x00\x00\x00\x0b\x00\x00\x00Elementx\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/506_DarkKnight/5067_DarkKnight_LOD2\x04\x00\x00\x00\x04\x00\x00\x00\x8f\x00\x00\x00\x0b\x00\x00\x00Elementx\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringJ\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Hero/506_DarkKnight/5067_DarkKnight_LOD3\x04\x00\x00\x00\x04\x00\x00\x00\xa4\x00\x00\x00\x16\x00\x00\x00ArtSkinPrefabLODEx0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00V\x00\x00\x00\x01\x00\x00\x00N\x00\x00\x00\x0b\x00\x00\x00Element7\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\t\x00\x00\x00\x05\x00\x00\x00V\x04\x00\x00\x00\x04\x00\x00\x00\x07\x02\x00\x00\x17\x00\x00\x00ArtSkinLobbyShowLOD0\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTArr\x1b\x00\x00\x00\x08\x00\x00\x00TypeSystem.String[]\x04\x00\x00\x00\xb8\x01\x00\x00\x03\x00\x00\x00\x90\x00\x00\x00\x0b\x00\x00\x00Elementy\x00\x00\x00\x03\x00\x00\x00\t\t<bool name="abortFilterSkill9" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="abortFilterMove" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="abortFilterDamage" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidMoveRotate" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="delaySkillAbort" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="protectAbortLevel" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xb8\x8d\xe4\xbf\x9d\xe6\x8a\xa4"/>\n\t\t\t\t\t<uint name="\xe4\xbf\x9d\xe6\x8a\xa4\xe5\xbb\xb6\xe8\xbf\x9f\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t\t<uint name="\xe4\xbf\x9d\xe6\x8a\xa4\xe5\xbc\xba\xe5\x88\xb6\xe6\x89\x93\xe6\x96\xad"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="ImmuneNegative" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="ImmuneControl" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidEnergyRecover" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="MoveIgnoreObstructArea" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidCollisionDetection" valu\n        <int name="SelfSkillCombineID_3" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombine_1" value="523000" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombine_2" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombineID1Probability" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombineID2Probability" value="0" refParamName="" useRefParam="false" />\r\n        <int name="TargetSkillCombineID3Probability" value="0" refParamName="" useRefParam="false" />\r\n        <bool name="bCheckSight" value="false" refParamName="" useRefParam="false" />\r\n        <bool name="bCheckSkillLevel" value="false" refParamName="" useRefParam="false" />\r\n        <Enum name="refSkillSlot" value="1" refParamName="" useRefParam="false">\r\n          <uint name="\xe6\x99\xae\xe6\x94\xbb" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd1" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd2" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd3" />\r\n          <uint name="\xe6\x8a\x80\xe8\x83\xbd4" />\r\n \x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x0f\x03\x00\x00\x19\x00\x00\x00particlesInOtherLayerw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.String,System.Int32]]\x04\x00\x00\x00w\x02\x00\x00\x02\x00\x00\x009\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xd2\x00\x00\x00\x02\x00\x00\x00\x81\x00\x00\x00\x06\x00\x00\x00v1o\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.StringA\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/New_Common_Effects/BlueTower_Bullet\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x006\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\xcf\x00\x00\x00\x02\x00\x00\x00~\x00\x00\x00\x06\x00\x00\x00v1l\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String>\x00\x00\x00\x05\x00\x00\x00VPrefab_Skill_Effects/New_Common_Effects/BlueTower_Hit\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00MSES\x07\x00\x00\x00\xbe\x00\x00\x00:\x00\x00\x00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00UTF-8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00189d89e27401dc8d9af987c9418892f7\x00\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x00\x00\xab\x00\x00\x00\x02\x00\x00\x00\x00\n\x00\x00\x005v5\xe5\x8c\xb9\xe9\x85\x8d\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00Param="false"/>\n\t\t\t\t<int name="particleScaleGrow" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="ReplacementUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x97\xa0"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t\t<uint name="\xe5\x87\xbb\xe6\x9d\x80\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t\t<uint name="\xe6\xb3\x89\xe6\xb0\xb4\xe5\x8a\xa0\xe9\x80\x9f\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t</Enum>\n\t\t\t\t<Enum name="ReplacementSubUsage" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x97\xa0"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e\xe8\x90\xbd\xe5\x9c\xb0\xe7\x89\xb9\xe6\x95\x88"/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bNoDynamicLod" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bMeshResouce" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAllowEmptyEffect" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="applyActionSpeedToParticle" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<int name="extend" value="10" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bOnlyFollowPos" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bRotateFollowCamera" value" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Condition id="0" guid="efdb163c-b41c-4d39-b682-49e0e463281a" status="true"/>\n\t\t\t<Event eventName="ForbidAbilityDuration" time="0.000" length="0.500" isDuration="true">\n\t\t\t\t<TemplateObject name="attackerId" objectName="target" id="1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidMove" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidSkill" value="true" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forceForbidding" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidSkillAndHideBtn" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill0" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill1" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill2" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="forbidFilterSkill3" valame="\xe5\xa4\xa9\xe8\xb5\x8b\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name="\xe5\x9b\x9e\xe5\x9f\x8e"/>\n\t\t\t\t\t<uint name="\xe9\xa5\xb0\xe5\x93\x81\xe6\xa0\x8f\xe6\x8a\x80\xe8\x83\xbd"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<int name="refSkillLevel" value="0" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="compareOPType" value="3" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe4\xb8\x8d\xe6\xaf\x94\xe8\xbe\x83"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xb0\x8f\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name="\xe5\xa4\xa7\xe7\xad\x89\xe4\xba\x8e"/>\n\t\t\t\t\t<uint name=""/>\n\t\t\t\t</Enum>\n\t\t\t\t<bool name="bFilterMajorMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterMinorMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterSoldier" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bFilterOtherMonster" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bAddEffectCount" value="true" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="HitTriggerDuration0" eventType="HitTriggerDuration" guid="f1307d98-07[System.String,System.Int32]\x04\x00\x00\x00\xf2\x00\x00\x00\x02\x00\x00\x00\xa1\x00\x00\x00\x06\x00\x00\x00v1\x8f\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.Stringa\x00\x00\x00\x05\x00\x00\x00VPrefab_Characters/Prefab_Organ/Tower/New_RedTower_High/skill/New_RedTower_High_A1E1_Slow\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x99\x01\x00\x00\x0c\x00\x00\x00skillIDsw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00\x0e\x01\x00\x00\x01\x00\x00\x00\x06\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\x9f\x00\x00\x00\x02\x00\x00\x00N\x00\x00\x00\x06\x00\x00\x00v1<\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0e\x00\x00\x00\x05\x00\x00\x00V75013\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\xb4\x04\x00\x00\x11\x00\x00\x00skillCombinesw\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCusb\x00\x00\x00\x08\x00\x00\x00TypeSystem.Collections.Generic.List`1[AssetRefAnalyser.Pair`2[System.UInt32,System.Int32]]\x04\x00\x00\x00$\x04\x00\x00\x04\x00\x00\x00\x07\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.UInt32,System.Int32]\x04\x00\x00\x00\xa0\x00\x00\x00\x02\x00\x00\x00O\x00\x00\x00\x06\x00\x00\x00v1=\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.UInt32\x0f\x00\x00\x00\x05\x00\x00\x00V750130\x04\x00\x00\x00\x04\x00\x00<TemplateObject name="VirtualAttachBulletId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bUseAttachBulletShape" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName" value="prefab_skill_effects/hero_skill_effects/502_astrid/astrid_natk01_hurt01" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName2" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="resourceName3" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<float name="lifeTime" value="1.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<String name="bindPointName" value="" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="bindPosOffset" x="0.000" y="1.000" z="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<EulerAngle name="bindRotOffset" x="0.000" y="0.000" z="0.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<Vector3 name="scaling" x="1.000" y="1.000" z="1.000" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="bEnableOptCull" value\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00\x05\x01\x00\x00\x0b\x00\x00\x00ElementT\x00\x00\x00\x02\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTCom?\x00\x00\x00\x08\x00\x00\x00TypeAssetRefAnalyser.Pair`2[System.String,System.Int32]\x04\x00\x00\x00\x9e\x00\x00\x00\x02\x00\x00\x00M\x00\x00\x00\x06\x00\x00\x00v1;\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x19\x00\x00\x00\x08\x00\x00\x00TypeSystem.String\r\x00\x00\x00\x05\x00\x00\x00VAtk2\x04\x00\x00\x00\x04\x00\x00\x00I\x00\x00\x00\x06\x00\x00\x00v27\x00\x00\x00\x03\x00\x00\x00\r\x00\x00\x00\x06\x00\x00\x00JTPri\x18\x00\x00\x00\x08\x00\x00\x00TypeSystem.Int32\n\x00\x00\x00\x05\x00\x00\x00V1\x04\x00\x00\x00\x04\x00\x00\x00PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x00\x00508_Zhadanren/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x14\x00\x00\x00508_Zhadanren/skill/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1b\x00\x00\x00508_Zhadanren/skill/extend/PK\x03\x04\n\x00\x00\x00\x00\x00\x00\x00!\x00\x11\xe7\x15!\x06x\x00\x00\x06x\x00\x00#\x00\x00\x00508_Zhadanren/skill/extend/exA4.xml<?xml version="1.0" encoding="utf-8"?>\n<Project>\n\t<TemplateObjectList>\n\t\t<TemplateObject objectName="self" id="0" isTemp="false"/>\n\t\t<TemplateObject objectName="target" id="1" isTemp="false"/>\n\t\t<TemplateObject objectName="bullet" id="2" isTemp="true"/>\n\t</TemplateObjectList>\n\t<RefParamList>\n\t\t<Vector3i name="targetdir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t\t<Vector3i name="_BulletDir" x="0" y="0" z="0" refParamName="" useRefParam="false"/>\n\t</RefParamList>\n\t<Action tag="" length="1.000" loop="false">\n\t\t<Tram="false"/>\n\t\t\t\t<bool name="bImmediateRotate" value="true" refParamName="" useRefParam="false"/>\n\t\t\t</Event>\n\t\t</Track>\n\t\t<Track trackName="SkillCDTriggerTick0" eventType="SkillCDTriggerTick" guid="ed9f0f3d-9931-4fb8-a5fa-b455c6cbe800" enabled="true" useRefParam="false" refParamName="" r="1.000" g="0.000" b="0.700" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">\n\t\t\t<Event eventName="SkillCDTriggerTick" time="0.000" isDuration="false">\n\t\t\t\t<TemplateObject name="targetId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<bool name="useSlotType" value="false" refParamName="" useRefParam="false"/>\n\t\t\t\t<Enum name="slotType" value="0" refParamName="" useRefParam="false">\n\t\t\t\t\t<uint name="\xe6\x99\xae\xe9\x80\x9a"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd1"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80\xe8\x83\xbd2"/>\n\t\t\t\t\t<uint name="\xe6\x8a\x80'
_ZSTD_LEVEL = 18

def decompress_(strin, zd=None):
    if zd is None:
        zd = _ZSTD_DICT
    pos = strin.find(b"\x28\xb5\x2f\xfd")
    if pos != -1:
        strin = strin[pos:]
        strin = strin[strin.find(b"\x28\xb5\x2f\xfd"):]
        strin = pyzstd.decompress(strin, pyzstd.ZstdDict(zd))
    return strin

def compress_(input_blob, zd=None, zl=None):
    if zd is None:
        zd = _ZSTD_DICT
    if zl is None:
        zl = _ZSTD_LEVEL
    if b'\x22\x4a\x67\x00' not in input_blob and b"\x28\xb5\x2f\xfd" not in input_blob:
        output_blob = bytearray(pyzstd.compress(input_blob, zl, pyzstd.ZstdDict(zd)))
        output_blob[0:0] = len(input_blob).to_bytes(4, byteorder="little", signed=False)
        output_blob[0:0] = b"\x22\x4a\x00\xef"
    else:
        output_blob = input_blob
    return output_blob

def get_last_two_digits(id_str):
    tail = id_str[-2:]
    return str(int(tail))

def fix_track_and_condition_ids(root):
    all_tracks = root.findall(".//Track")
    guid_to_index = {track.get("guid"): idx for idx, track in enumerate(all_tracks) if track.get("guid")}
    for condition in root.findall(".//Condition"):
        c_guid = condition.get("guid")
        if c_guid in guid_to_index:
            condition.set("id", str(guid_to_index[c_guid]))
    for track_obj in root.findall(".//TrackObject"):
        to_guid = track_obj.get("guid")
        if to_guid in guid_to_index:
            track_obj.set("id", str(guid_to_index[to_guid]))

def mod_binh_thuong(root, user_id, filename=''):
    is_modified = False
    all_tracks = root.findall(".//Track")
    skin_suffix = f"_Skin{get_last_two_digits(user_id)}"
    skip_guids_15013 = {
        'S11.xml': ['f06a1b3c-ef36-4b2d-a82b-a23832de40ff'],
        'S2.xml': ['b73050c0-0afc-4e3b-98e2-6ffe12d3d489'],
    }
    skip_guids_13314 = ['aa4cb49f-6c50-45f6-9922-de26fb2d1685', '37a5b5f5-aa40-4f6d-8b8f-22380bc7e51f', '156b19a5-3f62-479c-9711-0149cb854565']

    skip_guids_13213 = {
        'S1b0.xml': ['08997ed7-84c2-46d3-a51d-3f4c230bc6d7'],
    }
    for track in all_tracks:
        if track.get("enabled") == "false":
            continue
        fname = os.path.basename(filename)
        if user_id == '50119' and fname in ['death.xml', 'S1e3.xml']:
            continue
        if user_id == '50119' and re.match(r'A\d+\.xml', fname, re.IGNORECASE):
            continue
        if user_id == '11215' and fname in ['a1b2.xml', 'a2b1.xml', 'a2b2.xml', 'a4b1.xml', 'a4b2.xml', 's1b1.xml', 's1b3.xml']:
            continue
        if is_106xx(user_id) and fname.upper() == 'U1E1.XML':
            continue
        if user_id == '15013':
            if fname in skip_guids_15013 and track.get("guid") in skip_guids_15013[fname]:
                continue
        if user_id == '13314':
            if fname == 'U1.xml' and track.get("guid") in skip_guids_13314:
                continue

        if user_id == '13213':
            fname = os.path.basename(filename)
            if fname in skip_guids_13213 and track.get("guid") in skip_guids_13213[fname]:
                continue
            if fname == 'S1B1.xml':
                continue
        if user_id == '15015' and fname == 'U1.xml':
            skin_check = track.find(".//int[@name='skinId']")
            if skin_check is not None and skin_check.get("value") == '15015':
                continue
        if user_id in ['11120', '11119']:
            fname = os.path.basename(filename)
            if re.match(r'A\d+B\d+\.xml', fname, re.IGNORECASE) and track.get("guid") != "kiana-mod-aov-111":
                continue
        if track.get("eventType") == "PlayHeroSoundTick":
            event_name_tag = track.find(".//String[@name='eventName']")
            if event_name_tag is not None and event_name_tag.get("value"):
                current_val = event_name_tag.get("value")
                if not current_val.endswith(skin_suffix):
                    event_name_tag.set("value", current_val + skin_suffix)
                    is_modified = True
    for parent in root.findall('.//Track/..'):
        tracks_list = list(parent)
        inserted_count = 0
        for idx, track in enumerate(tracks_list):
            if track.tag != "Track":
                continue
            enabled_val = str(track.get("enabled")).lower()
            if enabled_val == "false":
                continue
            fname = os.path.basename(filename)
            if user_id == '50119' and fname in ['death.xml', 'S1e3.xml']:
                continue
            if user_id == '50119' and re.match(r'A\d+\.xml', fname, re.IGNORECASE):
                continue
            if user_id == '11215' and fname in ['a1b2.xml', 'a2b1.xml', 'a2b2.xml', 'a4b1.xml', 'a4b2.xml', 's1b1.xml', 's1b3.xml']:
                continue
            if is_106xx(user_id) and fname.upper() == 'U1E1.XML':
                continue
            if user_id == '15013' and fname in skip_guids_15013 and track.get("guid") in skip_guids_15013[fname]:
                continue
            if user_id == '13314' and fname == 'U1.xml' and track.get("guid") in skip_guids_13314:
                continue

            if user_id == '13213':
                if fname in skip_guids_13213 and track.get("guid") in skip_guids_13213[fname]:
                    continue
                if fname == 'S1B1.xml':
                    continue
            if user_id == '15015' and fname == 'U1.xml':
                skin_check = track.find(".//int[@name='skinId']")
                if skin_check is not None and skin_check.get("value") == '15015':
                    continue
            if user_id in ['11120', '11119'] and re.match(r'A\d+B\d+\.xml', fname, re.IGNORECASE) and track.get("guid") != "kiana-mod-aov-111":
                continue
            target_string = None
            for s_tag in track.findall(".//String"):
                name_attr = str(s_tag.get("name")).lower()
                val_attr = str(s_tag.get("value")).lower()
                if name_attr in ["resourcename", "prefab", "prefabname"] and "prefab_skill_effects/hero_skill_effects" in val_attr:
                    target_string = s_tag
                    break
            if target_string is not None:
                orig_value = target_string.get("value")
                ref_name = orig_value.split("/")[-1]
                target_string.set("refParamName", ref_name)
                target_string.set("useRefParam", "true")
                target_string.set("value", "")
                parts = orig_value.split("/")
                parts.insert(-1, user_id)
                new_holiday_path = "/".join(parts)
                new_track_guid = str(uuid.uuid4())
                new_track_xml = f"""
      <Track trackName="Mod_By_Kiana_Mod_Aov" eventType="GetHolidayResourcePathTick" guid="KIANAMOD-{new_track_guid}" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false">
         <Event eventName="GetHolidayResourcePathTick" time="0.000" isDuration="false">
            <String name="holidayResourcePathPrefix" value="{new_holiday_path}" refParamName="" useRefParam="false"/>
            <String name="outPathParamName" value="{ref_name}" refParamName="" useRefParam="false"/>
            <String name="outSoundEventParamName" value="" refParamName="" useRefParam="false"/>
         </Event>
      </Track>"""
                new_track_element = ET.fromstring(new_track_xml.strip())
                insert_pos = idx + inserted_count
                parent.insert(insert_pos, new_track_element)
                inserted_count += 1
                is_modified = True
    if is_modified:
        fix_track_and_condition_ids(root)
    return is_modified

def mod_dac_biet_1(root, user_id, filename=''):
    is_modified = False
    new_skin_id = "206" + user_id[3:] if len(user_id) > 3 else "206"
    fname = os.path.basename(filename)
    if user_id == '13213' and fname == 'S1B1.xml':
        return False
    skip_files = ['A2.xml', 'A5.xml', 'A7.xml', 'A8.xml', 'A9.xml']
    skip_guids_15013 = {
        'S11.xml': ['f06a1b3c-ef36-4b2d-a82b-a23832de40ff'],
        'S2.xml': ['b73050c0-0afc-4e3b-98e2-6ffe12d3d489'],
    }
    skip_guids_13314 = ['aa4cb49f-6c50-45f6-9922-de26fb2d1685', '37a5b5f5-aa40-4f6d-8b8f-22380bc7e51f', '156b19a5-3f62-479c-9711-0149cb854565']

    skip_guids_13213 = {
        'S1b0.xml': ['08997ed7-84c2-46d3-a51d-3f4c230bc6d7'],
    }
    for track in root.findall(".//Track"):
        if track.get("enabled") == "false":
            continue
        fname = os.path.basename(filename)
        if user_id == '50119' and fname in ['death.xml', 'S1e3.xml']:
            continue
        if user_id == '50119' and re.match(r'A\d+\.xml', fname, re.IGNORECASE):
            continue
        if user_id == '11215' and fname in ['a1b2.xml', 'a2b1.xml', 'a2b2.xml', 'a4b1.xml', 'a4b2.xml', 's1b1.xml', 's1b3.xml']:
            continue
        if is_106xx(user_id) and fname.upper() == 'U1E1.XML':
            continue
        if user_id == '15013':
            if fname in skip_guids_15013 and track.get("guid") in skip_guids_15013[fname]:
                continue
        if user_id == '13314':
            if fname == 'U1.xml' and track.get("guid") in skip_guids_13314:
                continue

        if user_id == '13213':
            if fname in skip_guids_13213 and track.get("guid") in skip_guids_13213[fname]:
                continue
            if fname == 'S1B1.xml':
                continue
        if user_id == '15015' and fname == 'U1.xml':
            skin_check = track.find(".//int[@name='skinId']")
            if skin_check is not None and skin_check.get("value") == '15015':
                continue
        if user_id in ['11120', '11119']:
            if re.match(r'A\d+B\d+\.xml', fname, re.IGNORECASE) and track.get("guid") != "kiana-mod-aov-111":
                continue
        skin_list = track.find(".//SkinOrAvatarList")
        if skin_list is not None and skin_list.get("id") == user_id:
            if user_id == '13706' and os.path.basename(filename) in skip_files:
                continue
            skip_skin_ids = ['13210', '14111', '10620', '10915', '13011', '14120', '15216', '19016', '19908', '52414', '59901', '59802']
            if skin_list.get("id") in skip_skin_ids:
                continue
            skin_list.set("id", new_skin_id)
            filter_type = track.get("SkinAvatarFilterType")
            if filter_type == "9":
                track.set("SkinAvatarFilterType", "11")
                is_modified = True
            elif filter_type == "11":
                track.set("SkinAvatarFilterType", "9")
                is_modified = True
            is_modified = True
    return is_modified

def mod_dac_biet_2(root, user_id, filename=''):
    is_modified = False
    new_skin_id = "206" + user_id[3:] if len(user_id) > 3 else "206"
    fname = os.path.basename(filename)
    if user_id == '13213' and fname == 'S1B1.xml':
        return False
    skip_guids_15013 = {
        'S11.xml': ['f06a1b3c-ef36-4b2d-a82b-a23832de40ff'],
        'S2.xml': ['b73050c0-0afc-4e3b-98e2-6ffe12d3d489'],
    }
    skip_guids_13314 = ['aa4cb49f-6c50-45f6-9922-de26fb2d1685', '37a5b5f5-aa40-4f6d-8b8f-22380bc7e51f', '156b19a5-3f62-479c-9711-0149cb854565']

    skip_guids_13213 = {
        'S1b0.xml': ['08997ed7-84c2-46d3-a51d-3f4c230bc6d7'],
    }
    for track in root.findall(".//Track"):
        if track.get("enabled") == "false":
            continue
        fname = os.path.basename(filename)
        if user_id == '50119' and fname in ['death.xml', 'S1e3.xml']:
            continue
        if user_id == '50119' and re.match(r'A\d+\.xml', fname, re.IGNORECASE):
            continue
        if user_id == '11215' and fname in ['a1b2.xml', 'a2b1.xml', 'a2b2.xml', 'a4b1.xml', 'a4b2.xml', 's1b1.xml', 's1b3.xml']:
            continue
        if is_106xx(user_id) and fname.upper() == 'U1E1.XML':
            continue
        if user_id == '15013':
            if fname in skip_guids_15013 and track.get("guid") in skip_guids_15013[fname]:
                continue
        if user_id == '13314':
            if fname == 'U1.xml' and track.get("guid") in skip_guids_13314:
                continue

        if user_id == '13213':
            if fname in skip_guids_13213 and track.get("guid") in skip_guids_13213[fname]:
                continue
            if fname == 'S1B1.xml':
                continue
        if user_id == '15015' and fname == 'U1.xml':
            skin_check = track.find(".//int[@name='skinId']")
            if skin_check is not None and skin_check.get("value") == '15015':
                continue
        if user_id in ['11120', '11119']:
            if re.match(r'A\d+B\d+\.xml', fname, re.IGNORECASE) and track.get("guid") != "kiana-mod-aov-111":
                continue
        skin_id_tag = track.find(".//int[@name='skinId']")
        if skin_id_tag is not None and skin_id_tag.get("value") == user_id:
            skip_skin_ids = ['13210', '14111', '10620', '10915', '13011', '14120', '15216', '19016', '19908', '52414', '59901', '59802']
            if skin_id_tag.get("value") in skip_skin_ids:
                continue
            skin_id_tag.set("value", new_skin_id)
            event_tag = track.find(".//Event")
            if event_tag is not None:
                b_equal_tag = event_tag.find("./bool[@name='bEqual'][@value='false']")
                negate_val_tag = event_tag.find("./bool[@name='useNegateValue'][@value='true']")
                has_deleted = False
                if b_equal_tag is not None:
                    event_tag.remove(b_equal_tag)
                    has_deleted = True
                if negate_val_tag is not None:
                    event_tag.remove(negate_val_tag)
                    has_deleted = True
                if not has_deleted:
                    event_type = track.get("eventType")
                    if event_type == "CheckSkinIdVirtualTick":
                        new_tag = ET.Element("bool", name="useNegateValue", value="true", refParamName="", useRefParam="false")
                        event_tag.append(new_tag)
                    elif event_type == "CheckSkinIdTick":
                        new_tag = ET.Element("bool", name="bEqual", value="false", refParamName="", useRefParam="false")
                        event_tag.append(new_tag)
                is_modified = True
    return is_modified

def is_106xx(user_id):
    return user_id.startswith('106')

def mod_106xx(root, user_id, filename=''):
    if not is_106xx(user_id):
        return False
    fname = os.path.basename(filename)
    if fname.upper() != 'U1E1.XML':
        return False
    is_modified = False
    skin_suffix = f"_Skin{get_last_two_digits(user_id)}"
    all_tracks = root.findall(".//Track")
    for track in all_tracks:
        if track.get("enabled") == "false":
            continue
        if track.get("eventType") == "PlayHeroSoundTick":
            event_name_tag = track.find(".//String[@name='eventName']")
            if event_name_tag is not None and event_name_tag.get("value"):
                current_val = event_name_tag.get("value")
                if not current_val.endswith(skin_suffix):
                    event_name_tag.set("value", current_val + skin_suffix)
                    is_modified = True
    for track in all_tracks:
        if track.get("enabled") == "false":
            continue
        for s_tag in track.findall(".//String"):
            name_attr = str(s_tag.get("name")).lower()
            val_attr = str(s_tag.get("value")).lower()
            if name_attr in ["resourcename", "prefab", "prefabname"] and "106_xiaoqiao" in val_attr:
                orig_val = s_tag.get("value")
                new_val = re.sub(r'106_[Xx]iaoqiao/', f'106_Xiaoqiao/{user_id}/', orig_val, flags=re.IGNORECASE)
                if new_val != orig_val:
                    s_tag.set("value", new_val)
                    is_modified = True
    return is_modified

def mod_tich_hop_hd(element):
    is_modified = False
    if element.get("enabled") == "false":
        return False
    if element.tag == "String" and element.get("name") in ["outPathParamName", "holidayResourcePathPrefix"]:
        current_value = element.get("value")
        if current_value and not current_value.endswith(".Prefab"):
            element.set("value", f"{current_value}.Prefab")
            is_modified = True
    elif element.tag == "String" and element.get("name") in ["resourceName", "prefab", "prefabName"]:
        current_ref = element.get("refParamName")
        if current_ref and not current_ref.endswith(".Prefab"):
            element.set("refParamName", f"{current_ref}.Prefab")
            is_modified = True
    for child in element:
        if mod_tich_hop_hd(child):
            is_modified = True
    return is_modified

def mod_dac_biet_15009_15015(root, user_id, filename):
    fname = os.path.basename(filename)
    if fname != 'U1.xml':
        return False
    is_modified = False
    all_tracks = root.findall(".//Track")
    for track in all_tracks:
        if track.get("enabled") == "false":
            continue
        if user_id in ['15009', '15015']:
            for tag in track.findall(".//bool[@name='bAllowEmptyEffect']"):
                if tag.get("value") == "true":
                    tag.set("value", "false")
                    is_modified = True
    if user_id == '15015':
        action = root.find(".//Action")
        action_tracks = list(action.findall(".//Track")) if action is not None else []
        for track in all_tracks:
            if track.get("enabled") == "false":
                continue
            skin_id_tag = track.find(".//int[@name='skinId']")
            if skin_id_tag is not None and skin_id_tag.get("value") == '15015':
                continue
            for cond in track.findall(".//Condition"):
                if cond.get("guid") == "e89a739d-ad18-433f-83c7-ed477652dd8f":
                    cond.set("guid", "c0b9dcbe-c83f-4a57-b203-70a202308416")
                    idx = action_tracks.index(track) if track in action_tracks else 0
                    cond.set("id", str(idx))
                    is_modified = True
                if cond.get("guid") == "bf4a4330-412d-4b5e-9a2f-723ba76bdffb":
                    cond.set("guid", "6e38b810-2c03-4c25-9331-fd09a03cb2e2")
                    idx = action_tracks.index(track) if track in action_tracks else 0
                    cond.set("id", str(idx))
                    is_modified = True
    return is_modified

def mod_11120_axbx(root, user_id, filename):
    if user_id not in ['11120', '11119']:
        return False
    fname = os.path.basename(filename)
    if not re.match(r'A\d+B\d+\.xml', fname, re.IGNORECASE):
        return False
    action = root.find(".//Action")
    if action is None:
        return False
    new_track_xml = '''<Track trackName="Them_vao" eventType="TriggerParticleTick" guid="kiana-mod-aov-111" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
      <Event eventName="TriggerParticleTick" time="0.000" isDuration="false" guid="0a4f6905-d82d-457b-8a9f-a7653020ed78">
        <TemplateObject name="objectSpaceId" objectName="\u653b\u51fb\u8005" id="0" isTemp="false" refParamName="" useRefParam="false"/>
        <TemplateObject name="targetId" objectName="None" id="-1" isTemp="false" refParamName="" useRefParam="false"/>
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/111_sunshangxiang/sunshangxiang_attack01_c" refParamName="" useRefParam="false"/>
        <bool name="bUseHeroLocalForward" value="true" refParamName="" useRefParam="false"/>
        <bool name="applyActionSpeedToAnimation" value="true" refParamName="" useRefParam="false"/>
        <float name="lifeTime" value="0.150" refParamName="" useRefParam="false"/>
        <Vector3i name="scalingInt" x="10000" y="10000" z="20000" refParamName="" useRefParam="false"/>
        <Vector3 name="bindPosOffset" x="0.300" y="0.650" z="0.600" refParamName="" useRefParam="false"/>
      </Event>
    </Track>'''
    new_track = ET.fromstring(new_track_xml)
    action.append(new_track)
    return True

def mod_13210_addtrack(root, user_id, filename):
    if user_id != '13210':
        return False
    fname = os.path.basename(filename)
    if fname not in ['S1b0.xml', 'S11b0.xml', 'S12b0.xml']:
        return False
    action = root.find(".//Action")
    if action is None:
        return False
    new_track_xml = '''<Track trackName="CheckRandomBuffTick0" eventType="CheckRandomBuffTick" guid="5be6c2e1-2c46-44c8-a381-ad092089be58" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true">
         <Event eventName="CheckRandomBuffTick" time="0.000" isDuration="false" guid="8b07e66f-faee-40d0-bb74-7665273e9657">
            <TemplateObject name="srcId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>
            <Array name="skillBuffIDArray" refParamName="" useRefParam="false" type="int">
               <int value="132116"/>
               <int value="132116"/>
               <int value="132116"/>
            </Array>
            <Array name="skillBuffIDEffectArray" refParamName="" useRefParam="false" type="int">
               <int value="132111"/>
               <int value="132112"/>
               <int value="132113"/>
            </Array>
         </Event>
      </Track>'''
    new_track = ET.fromstring(new_track_xml)
    action.append(new_track)
    return True

def mod_13213_addtrack(root, user_id, filename):
    if user_id != '13213':
        return False
    fname = os.path.basename(filename)
    action = root.find(".//Action")
    if action is None:
        return False
    if fname == 'S1b0.xml':
        new_track_xml = '''<Track trackName="CheckRandomBuffTick0" eventType="CheckRandomBuffTick" guid="9a6492cb-e3a0-4bea-9534-a5b0d46baee6" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" stopAfterLastEvent="true" >
      <Event eventName="CheckRandomBuffTick" time="0.000" isDuration="false" guid="8e14d03b-8a1c-4b5b-b941-93c6d2b8fde9">
        <TemplateObject name="srcId" objectName="self" id="0" isTemp="false" refParamName="" useRefParam="false"/>
        <Array name="skillBuffIDEffectArray" refParamName="" useRefParam="false" type="int">
          <int value="132111"/>
          <int value="132112"/>
          <int value="132113"/>
        </Array>
        <Array name="skillBuffIDArray" refParamName="" useRefParam="false" type="int">
          <int value="7790001"/>
        </Array>
        <int name="skillBuffIDEffectDefault" value="132113" refParamName="" useRefParam="false"/>
      </Event>
    </Track>'''
        new_track = ET.fromstring(new_track_xml)
        action.append(new_track)
        return True
    if fname == 'S1B1.xml':
        new_track_xml = '''<Track trackName="them_13213" eventType="TriggerParticle" guid="5d0b3f8d-7647-4004-aeab-c11f335181e5" enabled="true" useRefParam="false" refParamName="" r="0.000" g="0.000" b="0.000" execOnForceStopped="false" execOnActionCompleted="false" SkinAvatarFilterType="9">
      <Event eventName="TriggerParticle" time="0.000" length="0.700" isDuration="true" guid="e9d0a9d0-f6c5-4bdc-b111-8b1c612a4cf7">
        <TemplateObject name="targetId" objectName="bullet" id="2" isTemp="true" refParamName="" useRefParam="false"/>
        <String name="resourceName" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13213/makeboluo_attack_spell01a" refParamName="" useRefParam="false"/>
        <Vector3i name="scalingInt" x="10000" y="10000" z="10000" refParamName="" useRefParam="false"/>
        <String name="resourceName3" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13213/makeboluo_attack_spell01i" refParamName="" useRefParam="false"/>
        <String name="resourceName2" value="prefab_skill_effects/hero_skill_effects/132_makeboluo/13213/makeboluo_attack_spell01g" refParamName="" useRefParam="false"/>
        <String name="syncAnimationName" value="" refParamName="" useRefParam="false"/>
        <String name="customTagName" value="" refParamName="" useRefParam="false"/>
      </Event>
    </Track>'''
        new_track = ET.fromstring(new_track_xml)
        action.append(new_track)
        return True
    return False

# ---- Mod ngoai hinh (from a_1.py) ----
def hex_to_dec(a):
    a=a[::-1]
    a=a.hex()
    return int(a,16)

def dec_to_hex(a):
    a=hex(a)[2:]
    if len(a)%2==1:
        a='0'+a
    return (bytes.fromhex(a))[::-1]

def split_code_infos_a(a):
    z=[]
    p=a.find('\n      <Item Var="Com" Type="Assets.Scripts.GameLogic.SkinElement">')
    while p!=-1:
        p2=a.find('\n      </Item>',p)
        z.append(a[p+len('\n      <Item Var="Com" Type="Assets.Scripts.GameLogic.SkinElement">'):p2])
        p=a.find('\n      <Item Var="Com" Type="Assets.Scripts.GameLogic.SkinElement">\n         ',p2)
    return z

def mod_ef_sound2(a, nh_bytes, ID_bytes):
    z = []
    str1 = b"hero_skill_effects/" + nh_bytes.lower() + b"/"
    str2 = b"hero_skill_effects/" + nh_bytes + b"/"
    str3 = b"Hero_Skill_Effects/" + nh_bytes.lower() + b"/"
    str4 = b"Hero_Skill_Effects/" + nh_bytes + b"/"
    z.append(str1); z.append(str2); z.append(str3); z.append(str4)
    strsp = b"component_effects/"
    if ID_bytes in [b'13311', b'16707', b'11620']:
        for b in z:
            if b in a:
                a = a.replace(b, strsp + ID_bytes + b'/' + ID_bytes + b'_5/')
    else:
        for b in z:
            if b in a:
                a = a.replace(b, b + ID_bytes + b'/')
    if ID_bytes[:3] == b'190':
        a = a.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/190_Zhugeliang/', b'Prefab_Skill_Effects/Hero_Skill_Effects/190_Zhugeliang/' + ID_bytes + b'/')
    if ID_bytes == b'15412':
        a = a.replace(b'Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15412/15413_HuaMuLan_Red', b'Prefab_Skill_Effects/Hero_Skill_Effects/154_HuaMuLan/15413_HuaMuLan_Red')
    a = a.replace(b'        <bool name="bAllowEmptyEffect" value="true" refParamName="" useRefParam="false" />\r\n', b'        <bool name="bAllowEmptyEffect" value="false" refParamName="" useRefParam="false" />\r\n')
    return a

def fix_ef_infos(a, nh, ID):
    a = mod_ef_sound2(a.encode('utf-8'), nh.encode('utf-8'), ID.encode('utf-8')).decode()
    str_variants = [
        "hero_skill_effects/" + nh.lower() + "/",
        "hero_skill_effects/" + nh + "/",
        "Hero_Skill_Effects/" + nh.lower() + "/",
        "Hero_Skill_Effects/" + nh + "/",
    ]
    for b in str_variants:
        if b in a:
            a = a.replace(b, b + ID + '/')
    if ID[:3] == '190':
        a = a.replace('Prefab_Skill_Effects/Hero_Skill_Effects/190_Zhugeliang/', 'Prefab_Skill_Effects/Hero_Skill_Effects/190_Zhugeliang/' + ID + '/')
    p = a.find('/' + ID + '/' + ID + '/')
    while p != -1:
        a = a.replace('/' + ID + '/' + ID + '/', '/' + ID + '/')
        p = a.find('/' + ID + '/' + ID + '/')
    return a

def mod_infos_mac_dinh(a, skinid, skin_list, SoInfos=0):
    if skinid == '13311':
        a = a.replace('Prefab_Characters/Prefab_Hero/133_DiRenJie/1332_DiRenJie_LOD', 'Prefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_LOD').replace('Prefab_Characters/Prefab_Hero/133_DiRenJie/1332_DiRenJie_Show', 'Prefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_04_Show').replace('Prefab_Characters/Prefab_Hero/133_DiRenJie/1331_DiRenJie_Cam', 'Prefab_Characters/Prefab_Hero/133_DiRenJie/Awaken/13312_DiRenJie_AW5_Cam')
    if skinid == '16707':
        a = a.replace('Prefab_Characters/Prefab_Hero/167_WuKong/1678_SunWuKong_AW1_LOD', 'Prefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_sunwukong_03_LOD').replace('Prefab_Characters/Prefab_Hero/167_WuKong/1678_SunWuKong_AW1_Show', 'Prefab_Characters/Prefab_Hero/167_WuKong/Awaken/1678_sunwukong_03_Show').replace('Prefab_Characters/Prefab_Hero/167_WuKong/1678_SunWuKong_AW1_Cam</ArtSkinLobbyShowCamera>', 'Prefab_Characters/Prefab_Hero/167_wukong/Awaken/1678_sunwukong_03_Cam</ArtSkinLobbyShowCamera>\n         <ArtSkinLobbyShowMovie Var="String" Type="System.String">Prefab_Characters/Prefab_Hero/167_wukong/Awaken/1678_sunwukong_03_Movie</ArtSkinLobbyShowMovie>')
    if skinid == '11620':
        a = a.replace('Prefab_Characters/Prefab_Hero/116_JingKe/11621_JingKe_AW1_Show', 'Prefab_Characters/Prefab_Hero/116_JingKe/Awaken/11621_JingKe_04_Show').replace('Prefab_Characters/Prefab_Hero/116_JingKe/Awaken/11621_JingKe_AW1_Cam</ArtSkinLobbyShowCamera>', 'Prefab_Characters/Prefab_Hero/116_JingKe/Awaken/11621_JingKe_AW1_Cam</ArtSkinLobbyShowCamera>\n         <ArtSkinLobbyShowMovie Var="String" Type="System.String">Prefab_Characters/Prefab_Hero/116_JingKe/Awaken/11621_JingKe_Movie</ArtSkinLobbyShowMovie>')
        a = a.replace('AW1', 'AW5')
    skinid2 = skinid[:3] + str(int(skinid[3:]) + 1)
    for skin in split_code_infos_a(a):
        if SoInfos != 0:
            if 'Assets.Scripts.GameLogic.EAntiAliasing' not in skin:
                a = a.replace(skin, skin.replace('         </ArtSkinLobbyShowLOD>', f'         </ArtSkinLobbyShowLOD>\n         <MSAA Var="Enum" Type="Assets.Scripts.GameLogic.EAntiAliasing">{SoInfos}</MSAA>'))
            else:
                match = re.search(r'<MSAA Var="Enum" Type="Assets.Scripts.GameLogic.EAntiAliasing">(.*?)</MSAA>', a)
                if match:
                    a = a.replace(skin, skin.replace(f'<MSAA Var="Enum" Type="Assets.Scripts.GameLogic.EAntiAliasing">{match.group(1)}</MSAA>', f'<MSAA Var="Enum" Type="Assets.Scripts.GameLogic.EAntiAliasing">{SoInfos}</MSAA>'))
    for skin in split_code_infos_a(a):
        p = skin.find('_Show')
        if f'/{skinid2}_' in skin[:p]:
            break
    skin = skin.replace('<ArtSkinPrefabLOD ', '<ArtPrefabLOD ').replace('</ArtSkinPrefabLOD>', '</ArtPrefabLOD>').replace('<ArtSkinLobbyShowLOD ', '<ArtLobbyShowLOD ').replace('</ArtSkinLobbyShowLOD>', '</ArtLobbyShowLOD>')
    skin = skin[skin.find('<ArtPrefabLOD '):]
    skin = skin.replace('>\n      ', '>\n')
    p2 = a.find('\n   <SkinPrefab ')
    if skinid2 in ['5486', '1749']:
        p = a.find('</ActorName>\n   ')
        de = a[p + len('</ActorName>\n   '):p2]
        skin = skin.replace('useNewMecanim', 'oriSkinUseNewMecanim')
    else:
        p = a.find('<ArtPrefabLOD ')
        de = a[p:p2]
    a = a.replace(de, skin, 1)
    for skin_full in split_code_infos_a(a):
        p = skin_full.find('_Show')
        if f'/{skinid2}_' in skin_full[:p]:
            break
    skin = skin_full
    for i in split_code_infos_a(a):
        match = re.search(r"Prefab_Characters/Prefab_Hero/.*/(\d+)_", i)
        if match:
            id_de = match.group(1)
            id_de = str(int(id_de[:3]) * 100 + int(id_de[3:]) - 1)
            if id_de.encode('utf-8') in skin_list:
                a = a.replace(i, skin, 1)
    return a

def ten_skin_hieu_ung(skinid):
    try:
        with open('./KIANA_AOV/Resources/1.62.1/Databin/Client/Actor/heroSkin.bytes', 'rb') as f:
            a = f.read()
        a = decompress_(a, _ZSTD_DICT) if _ZSTD_DICT else a
        p = a.find(dec_to_hex(skinid) + b'\x00\x00' + dec_to_hex(int(str(skinid)[:3])))
        ten = b''; skin = b''; bien_ve_ef = False
        if p != -1:
            ten = a[p+12:p+31]
            skin = a[p+40:p+59]
            code = a[p-4:p+hex_to_dec(a[p-4:p-2])]
            if b"Skin_Icon_Skill" in code or b"Skin_Icon_BackToTown" in code or skinid in [53702, 13204, 15305, 13706]:
                h = b'\x8f'
            else:
                h = b'KianaMod'
                try:
                    with open('./KIANA_AOV/Resources/1.62.1/Databin/Client/Sound/BattleBank.bytes', 'rb') as fb:
                        ab = fb.read()
                    ab = decompress_(ab, _ZSTD_DICT) if _ZSTD_DICT else ab
                    if bytes(str(skinid), 'utf-8') in ab:
                        h = b'\x8f'
                except: pass
            if b"Skin_Icon_BackToTown" in code or b"Skin_Icon_Animation" in code:
                bien_ve_ef = True
            if skinid in [13204, 53702, 15305, 13706]:
                h = b'\x8f'
        a1 = ''; a2 = ''
        if ten != b'' and skin != b'':
            lang_dir = './KIANA_AOV/Resources/1.62.1/Languages/VN_Garena_VN'
            if os.path.isdir(lang_dir):
                for fn in os.listdir(lang_dir):
                    with open(f'{lang_dir}/{fn}', 'rb') as ft:
                        txt = ft.read()
                    txt = decompress_(txt, _ZSTD_DICT) if _ZSTD_DICT else txt
                    p1 = txt.find(ten)
                    if p1 != -1:
                        a1 = txt[p1+len(ten)+3:txt.find(b'\r', p1)].decode()
                    p2 = txt.find(skin)
                    if p2 != -1:
                        a2 = txt[p2+len(skin)+3:txt.find(b'\r', p2)].decode()
            if skinid == 50118:
                h = b'\x8f'
        return h, f'{a1} {a2}', bien_ve_ef
    except Exception as e:
        return b'KianaMod', '', False

def infoAboutSkin(skinid_bytes):
    try:
        with open('./KIANA_AOV/Resources/1.62.1/Databin/Client/Actor/heroSkin.bytes', 'rb') as f:
            a = f.read()
        a = decompress_(a, _ZSTD_DICT) if _ZSTD_DICT else a
        skin_list = [skinid_bytes[:3] + b'00']
        for i in range(1, 30):
            ID = int(skinid_bytes[:3].decode()) * 100 + i
            IDb = str(ID).encode('utf-8')
            p = a.find(dec_to_hex(int(IDb.decode())) + b'\x00\x00' + dec_to_hex(int(IDb[:3].decode())))
            if p != -1:
                code = a[p-4:p+hex_to_dec(a[p-4:p-2])]
                if b'Share' in code:
                    skin_list.append(IDb)
        SoInfos = 0
        p = a.find(dec_to_hex(int(skinid_bytes.decode())) + b'\x00\x00' + dec_to_hex(int(skinid_bytes[:3].decode())))
        if p != -1:
            code = a[p-4:p+hex_to_dec(a[p-4:p-2])]
            pshare = code.find(b'Share')
            if pshare != -1:
                ca = code[pshare-4:]
                for _ in range(4):
                    dem = hex_to_dec(ca[:2])
                    ca = ca[dem+4:]
                SoInfos = hex_to_dec(ca[:2])
        return skin_list, SoInfos
    except Exception as e:
        return [skinid_bytes[:3] + b'00'], 0



class BinaryXMLParser:
    def __init__(self, data):
        self.byt = io.BytesIO(data)
        self.i = 0
        self.nod = {}
        self.root = None

    def getint(self):
        return int.from_bytes(self.byt.read(4), 'little')

    def getstr(self, pos=None):
        if pos is not None:
            self.byt.seek(pos, 0)
        ofs = self.getint()
        stri = self.byt.read(ofs - 4)
        return stri.decode()

    def checkfour(self):
        if self.getint() != 4:
            self.byt.seek(-4, 1)

    def analyattr(self, pos=None):
        if pos is None:
            pos = self.byt.tell()
        else:
            self.byt.seek(pos, 0)
        ofs = self.getint()
        tp = self.getint()
        if tp == 5:
            stri = self.byt.read(ofs - 8).decode()[1:]
            self.checkfour()
            self.byt.seek(pos + ofs, 0)
            return stri
        else:
            if tp == 6:
                stri = self.byt.read(ofs - 8).decode()
                if stri[0:2] == 'JT':
                    if stri == 'JTArr':
                        stri = 'Array'
                    elif stri == 'JTPri':
                        stri = 'String'
                    else:
                        stri = stri[2:]
                    name = 'Var'
                else:
                    name = 'Var_Raw'
            elif tp == 8:
                stri2 = self.byt.read(ofs - 8).decode()
                if stri2[0:4] == 'Type':
                    stri = stri2[4:]
                    name = 'Type'
                else:
                    stri = stri2
                    name = 'Type_Raw'
            else:
                stri = self.byt.read(ofs - 8).decode()
                name = str(tp)
                self.byt.seek(pos + ofs, 0)
            return {name: stri}

    def analynode(self, fid=None, sta=None):
        if sta is None:
            sta = self.byt.tell()
        else:
            self.byt.seek(sta, 0)
        ofs = self.getint()
        stri = self.getstr()
        if stri == 'Element':
            stri1 = 'Item'
        else:
            stri1 = stri
        myid = self.i
        self.i += 1
        self.byt.seek(4, 1)
        aidx = self.getint()
        ite = False
        attr = {}
        text1 = ''
        for j in range(0, aidx):
            attr1 = self.analyattr()
            if type(attr1) == str:
                text1 = attr1
                ite = True
            else:
                attr.update(attr1)
        if fid is None:
            self.nod[myid] = ET.SubElement(self.root, stri1, attrib=attr)
        else:
            self.nod[myid] = ET.SubElement(self.nod[fid], stri1, attrib=attr)
        if ite:
            if text1 == '':
                self.nod[myid].text = ' '
            else:
                self.nod[myid].text = text1
        self.checkfour()
        chk = sta + ofs - self.byt.tell()
        if chk > 12:
            self.byt.seek(4, 1)
            sidx = self.getint()
            for h in range(0, sidx):
                self.analynode(myid, self.byt.tell())
        self.byt.seek(sta + ofs, 0)

    def parse(self):
        self.i = 0
        self.nod = {}
        ofs = self.getint()
        stri = self.getstr()
        if stri == 'Element':
            stri1 = 'Item'
        else:
            stri1 = stri
        self.root = ET.Element(stri1)
        self.byt.seek(4, 1)
        aidx = self.getint()
        ite = False
        attr = {}
        text1 = ''
        for j in range(0, aidx):
            attr1 = self.analyattr()
            if type(attr1) == str:
                text1 = attr1
                ite = True
            else:
                attr.update(attr1)
            self.root.attrib.update(attr)
        if ite:
            if text1 == '':
                self.root.text = ' '
            else:
                self.root.text = text1
        self.checkfour()
        chk = ofs - self.byt.tell()
        if chk > 12:
            self.byt.seek(4, 1)
            sidx = self.getint()
            for h in range(0, sidx):
                self.analynode(None, self.byt.tell())
        return self.root


def byteint(num):
    return num.to_bytes(4, byteorder='little')

def bytestr(stri):
    outbyte = byteint(len(stri) + 4)
    outbyte = outbyte + stri.encode()
    return outbyte

def byteattr(key, attr):
    if key == 'Var':
        if attr[key] == 'Array':
            stri = 'JTArr'
        elif attr[key] == 'String':
            stri = 'JTPri'
        else:
            stri = 'JT' + attr[key]
        aid = 6
    elif key == 'Var_Raw':
        stri = attr[key]
        aid = 6
    elif key == 'Type':
        stri = 'Type' + attr[key]
        aid = 8
    elif key == 'Type_Raw':
        stri = attr[key]
        aid = 8
    else:
        import unicodedata
        if unicodedata.numeric(key):
            stri = attr[key]
            aid = int(key)
    stripro = stri.encode()
    outbyte = byteint(len(stripro) + 8) + byteint(aid) + stripro
    return outbyte

def bytenode(node):
    iftex = False
    if node.tag == 'Item':
        name1 = 'Element'
    else:
        name1 = node.tag
    name = bytestr(name1)
    attr1 = b''
    aindex = len(node.attrib)
    plus = 8
    for key in node.attrib:
        attr1 = attr1 + byteattr(key, node.attrib)
    if (node.text is not None) and (node.text[0:1] != '\n'):
        if node.text == ' ':
            stri1 = ''
        else:
            stri1 = node.text
        iftex = True
        stripro = ('V' + stri1).encode()
        attr1 = attr1 + byteint(len(stripro) + 8) + byteint(5) + stripro + byteint(4)
        aindex += 1
        plus = 4
    attr1 = byteint(len(attr1) + plus) + byteint(aindex) + attr1 + byteint(4)
    alchild = b''
    if len(node):
        cindex = 0
        for child in node:
            alchild = alchild + bytenode(child)
            cindex += 1
        alchild = byteint(len(alchild) + 8) + byteint(cindex) + alchild
    else:
        if iftex is False:
            alchild = byteint(4)
    bnode = name + attr1 + alchild
    bnode = byteint(len(bnode) + 4) + bnode
    return bnode


def process_ngoai_hinh(uid, hero_folder, hd, zd):
    prefab_src = f'./KIANA_AOV/Resources/1.62.1/Prefab_Characters/Prefab_Hero/{hero_folder}'
    prefab_dst = f'./File_mod/Resources/1.62.1/Prefab_Characters/Prefab_Hero/{hero_folder}'
    os.makedirs(prefab_dst, exist_ok=True)
    if not os.path.isdir(prefab_src):
        return False, None
    skinid_bytes = uid.encode()
    skin_list, SoInfos = infoAboutSkin(skinid_bytes)
    file2 = None
    file3 = None
    for file in os.listdir(prefab_src):
        with open(f'{prefab_src}/{file}', 'rb') as f:
            a = f.read()
        if 'trap' in file.lower() or 'Trap' in file:
            a = decompress_(a, zd)
            file3 = file
        elif len(file) == len(hero_folder) + len('_actorinfo.bytes'):
            a = decompress_(a, zd)
            file2 = file
        with open(f'{prefab_dst}/{file}', 'wb') as f:
            f.write(a)
    thu = False
    try:
        if file2:
            filexml = f'{prefab_dst}/{file2}'
            with open(filexml, 'rb') as f:
                data = f.read()
            parser = BinaryXMLParser(data)
            root = parser.parse()
            xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
            xmlstr = mod_infos_mac_dinh(xmlstr, uid, skin_list, SoInfos)
            if hd:
                xmlstr = xmlstr.replace('_LOD2', '_LOD1').replace('_LOD3', '_LOD1')
                xmlstr = xmlstr.replace('_Show2', '_Show1').replace('_Show3', '_Show1')
            xmlstr = fix_ef_infos(xmlstr, hero_folder, uid)
            if skinid_bytes in [b'18402',b'18404',b'18405',b'18406',b'18407',b'18408',b'53402',b'53405',b'54801',b'54802',b'54803',b'54804',b'53701',b'53702',b'11610',b'11611',b'53902',b'53903',b'53904',b'53502',b'53504',b'53510',b'53602',b'53605',b'53606',b'53608',b'53609']:
                p = xmlstr.find('</bUnityLight>')
                if p != -1:
                    xmlstr = xmlstr.replace('True</bUnityLight>', 'False</bUnityLight>', 1)
            if skinid_bytes == b'19015':
                xmlstr = xmlstr.replace('\n   <useMecanim Var="String" Type="System.Boolean">True</useMecanim>', '', 1)
            if skinid_bytes in [b'54402']:
                xmlstr = xmlstr.replace('True</useTimeline>', 'False</useTimeline>', 1).replace('\n   <TransConfigs Var="Array" Type="Assets.Scripts.GameLogic.TransformConfig[]">\n      <Item Var="Com" Type="Assets.Scripts.GameLogic.TransformConfig"/>\n      <Item Var="Com" Type="Assets.Scripts.GameLogic.TransformConfig"/>\n   </TransConfigs>\n   <LookAt Var="Com" Type="Assets.Scripts.GameLogic.CameraLookAt">\n      <Offset Var="Com" Type="UnityEngine.Vector3">\n         <x Var="String" Type="System.Single">-0.07700014</x>\n         <y Var="String" Type="System.Single">1.689991</y>\n         <z Var="String" Type="System.Single">-1.183998</z>\n      </Offset>\n      <Direction Var="Com" Type="UnityEngine.Vector3">\n         <x Var="String" Type="System.Single">0.144031</x>\n         <y Var="String" Type="System.Single">0</y>\n         <z Var="String" Type="System.Single">0.9895732</z>\n      </Direction>\n      <Duration Var="String" Type="System.Single">1</Duration>\n   </LookAt>\n   <LightConfig Var="Com" Type="Assets.Scripts.GameLogic.PrepareBattleLightConfig"/>\n   <IdleShowConfigs Var="Array" Type="Assets.Scripts.GameLogic.IdleShowConfig[]">\n      <Item Var="Com" Type="Assets.Scripts.GameLogic.IdleShowConfig">\n         <DisableDirLight Var="String" Type="System.Boolean">True</DisableDirLight>\n      </Item>\n      <Item Var="Com" Type="Assets.Scripts.GameLogic.IdleShowConfig">\n         <DisableDirLight Var="String" Type="System.Boolean">True</DisableDirLight>\n      </Item>\n      <Item Var="Com" Type="Assets.Scripts.GameLogic.IdleShowConfig"/>\n   </IdleShowConfigs>', '', 1)
            if skinid_bytes in [b'12912']:
                xmlstr = xmlstr.replace('\n   <LobbyScale Var="String" Type="System.Single">1</LobbyScale>', '\n   <useStateDrivenMecanim Var="String" Type="System.Boolean">True</useStateDrivenMecanim>', 1)
            with open(filexml, "w", encoding="utf-8") as f:
                f.write(xmlstr)
            tree = ET.parse(filexml)
            byt_data = bytenode(tree.getroot())
            byt_data = byt_data.replace(b'\x5f\x4c\x4f\x44\x32', b'\x5f\x4c\x4f\x44\x31').replace(b'\x5f\x4c\x4f\x44\x33', b'\x5f\x4c\x4f\x44\x31')
            with open(filexml, 'wb') as f:
                f.write(byt_data)
        thu = False
    except Exception as e:
        print('mod infos loi: ', e)
        traceback.print_exc()
        thu = True
        byt_data = b''
    try:
        if b'</Item>' in byt_data:
            thu = True
    except:
        if '</Item>' in str(byt_data):
            thu = True
    if thu:
        try:
            if file2:
                strin = open(f'{prefab_src}/{file2}', 'rb').read()
                strin = decompress_(strin, zd)
                skinid_infos = uid[:3] + str(int(uid[3:]) + 1)
                pos = strin.find(b'ElementE')
                mac_dinh = strin[:pos - 109]
                skinprefabg2 = skinprefabg = strin[pos - 109:pos - 8]
                while pos != -1:
                    skin = strin[pos - 8:pos - 8 + hex_to_dec(strin[pos - 8:pos - 6])]
                    if b'/' + skinid_infos.encode() + b'_' in skin:
                        break
                    pos = strin.find(b'ElementE', pos + hex_to_dec(strin[pos - 8:pos - 6]) - 8)
                pos = mac_dinh.find(b'ArtPrefabLOD')
                pos2 = mac_dinh.find(b'LOD3', pos)
                lod_mac_dinh = mac_dinh[pos - 8:pos2 + 4]
                pos = mac_dinh.find(b'ArtLobbyShowLOD')
                pos2 = mac_dinh.find(b'Show3', pos)
                show_mac_dinh = mac_dinh[pos - 8:pos2 + 5]
                pos = skin.find(b'ArtSkinPrefabLOD')
                pos2 = skin.find(b'LOD3')
                lod_skin = skin[pos - 8:pos2 + 4].replace(b'ArtSkinPrefabLOD', b'ArtPrefabLOD')
                lod_skin = dec_to_hex(hex_to_dec(lod_skin[:2]) - 4) + lod_skin[2:]
                lod_skin = lod_skin[:4] + dec_to_hex(hex_to_dec(lod_skin[4:6]) - 4) + lod_skin[5:]
                pos = skin.find(b'ArtSkinLobbyShowLOD')
                pos2 = skin.find(b'Show3', pos)
                show_skin = skin[pos - 8:pos2 + 5].replace(b'ArtSkinLobbyShow', b'ArtLobbyShow')
                show_skin = dec_to_hex(hex_to_dec(show_skin[:2]) - 4) + show_skin[2:]
                show_skin = show_skin[:4] + dec_to_hex(hex_to_dec(show_skin[4:6]) - 4) + show_skin[5:]
                cam_skin_find = skin.find(b'ArtSkinLobbyShowCamera')
                if cam_skin_find != -1:
                    cam_skin = skin[cam_skin_find - 16:cam_skin_find + hex_to_dec(skin[cam_skin_find - 8:cam_skin_find - 6]) - 16]
                    use_find = skin.find(b'useNewMecanim')
                    if use_find != -1:
                        useNew = skin[use_find - 16:use_find + 73]
                    else:
                        use_find = skin.find(b'ArtSkinLobbyShowMovie')
                        if use_find != -1:
                            useNew = skin[use_find - 16:use_find + hex_to_dec(skin[use_find - 8:use_find - 6]) - 16]
                        else:
                            useNew = b''
                    cam_mac_dinh_find = mac_dinh.find(b'ArtSkinLobbyShowCamera')
                    if cam_mac_dinh_find != -1:
                        cam_mac_dinh = mac_dinh[cam_mac_dinh_find - 16:cam_mac_dinh_find + hex_to_dec(mac_dinh[cam_mac_dinh_find - 8:cam_mac_dinh_find - 6]) - 16]
                        strin = strin.replace(mac_dinh, mac_dinh.replace(lod_mac_dinh, lod_skin).replace(show_mac_dinh, show_skin).replace(cam_mac_dinh, cam_skin + useNew))
                    else:
                        strin = strin.replace(mac_dinh, mac_dinh.replace(lod_mac_dinh, lod_skin).replace(show_mac_dinh, show_skin))
                else:
                    strin = strin.replace(mac_dinh, mac_dinh.replace(lod_mac_dinh, lod_skin).replace(show_mac_dinh, show_skin))
                strin = strin.replace(b'\x5f\x4c\x4f\x44\x32', b'\x5f\x4c\x4f\x44\x31').replace(b'\x5f\x4c\x4f\x44\x33', b'\x5f\x4c\x4f\x44\x31')
                if uid == '54402':
                    strin = strin.replace(b'useTimeline', b'use0000line')
                with open(f'{prefab_dst}/{file2}', 'wb') as f:
                    f.write(strin)
        except Exception as bug:
            print(bug)
    try:
        if file3:
            filexml = f'{prefab_dst}/{file3}'
            with open(filexml, 'rb') as f:
                data = f.read()
            parser = BinaryXMLParser(data)
            root = parser.parse()
            xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
            for i in range(10):
                t = uid[:3] + '0' + str(i)
                if xmlstr.find(t) != -1:
                    xmlstr = xmlstr.replace(f'/{t}/', '/')
            xmlstr = mod_ef_sound2(xmlstr.encode('utf-8'), hero_folder, uid).decode()
            with open(filexml, "w", encoding="utf-8") as f:
                f.write(xmlstr)
            tree = ET.parse(filexml)
            byt_data = bytenode(tree.getroot())
            with open(filexml, 'wb') as f:
                f.write(byt_data)
    except Exception as bug:
        print('mod trap loi:', bug)
    return True, skin_list

def back_need(a):
    b=0;za=b''
    p=a.find(b'    <Track trackName=')
    while p!=-1 and b!=5:
        p2=a.find(b'    </Track>',p)
        z=a[p:p2+14]
        if b'clipName' in z:
            za+=z
            b+=1
        p=a.find(b'    <Track trackName=',p2)
    return za

def process_common_resources(src_base, dst_base, hd, zd):
    common_folders = ['commonresource', 'KeySpell', 'PassiveResource', 'mowen', 'Ultrafire', 'SeasonPlay']
    decompress_xml = ['BlueBuff.xml', 'RedBuff_Slow.xml', 'Born.xml', 'Back.xml', 'Dance.xml', 'HasteE1.xml', 'HasteE1_leave.xml']
    for fo in common_folders:
        src_dir = os.path.join(src_base, fo)
        dst_dir = os.path.join(dst_base, fo)
        if fo == 'SeasonPlay':
            if os.path.isdir(src_dir):
                if os.path.exists(dst_dir):
                    shutil.rmtree(dst_dir)
                shutil.copytree(src_dir, dst_dir)
            continue
        os.makedirs(dst_dir, exist_ok=True)
        if not os.path.isdir(src_dir):
            continue
        for file in os.listdir(src_dir):
            src_file = os.path.join(src_dir, file)
            dst_file = os.path.join(dst_dir, file)
            if hd and file in decompress_xml:
                with open(src_file, 'rb') as f:
                    data = f.read()
                    data = decompress_(data, zd)
                with open(dst_file, 'wb') as f:
                    f.write(data)
            else:
                shutil.copy2(src_file, dst_file)
    return True

def process_databin(src_base, dst_base, hd, zd):
    databin_folders = ['Sound','Actor','Skill','Shop','Motion','Huanhua']
    databin_files = ['BattleBank.bytes','ChatSound.bytes','HeroSound.bytes','LobbyBank.bytes','LobbySound.bytes','heroSkin.bytes','HeroSkinShop.bytes','liteBulletCfg.bytes','skillmark.bytes','ResSkinMotionBaseCfg.bytes','ResKillBillboardCfg.bytes','ResPersonalButtonCfg.bytes','organSkin.bytes']
    for data in databin_folders:
        for file in databin_files:
            src_path = os.path.join(src_base, data, file)
            dst_path = os.path.join(dst_base, data, file)
            if not os.path.exists(src_path):
                continue
            os.makedirs(os.path.dirname(dst_path), exist_ok=True)
            if hd:
                with open(src_path, 'rb') as f:
                    strin = f.read()
                    strin = decompress_(strin, zd)
                with open(dst_path, 'wb') as f:
                    f.write(strin)
            else:
                shutil.copy2(src_path, dst_path)
    for file in ['ResAwakenBattleSound.bytes','ResAwakenBattleEffect.bytes']:
        dst_path = os.path.join(dst_base, 'Actor', file)
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        with open(dst_path, 'wb') as f:
            f.write(b'\x4D\x53\x45\x53\x07\x00\x00\x00\x5B\x00\x00\x00\x00\x00\x00\x00\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x61\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x55\x54\x46\x2D\x38\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x4D\x4F\x44\x42\x59\x5F\x59\x54\x5F\x4B\x49\x41\x4E\x41\x5F\x4D\x4F\x44\x5F\x41\x4F\x56\x5F\x44\x4F\x4E\x54\x5F\x52\x45\x55\x50\x00\x00\x00\x00\x8C\x00\x00\x00\x00\x00\x00\x00')

    return True

def fix_ef(data, skin_id):
    p = data.find(b'/' + skin_id + b'/' + skin_id + b'/')
    while p != -1:
        data = data.replace(b'/' + skin_id + b'/' + skin_id + b'/', b'/' + skin_id + b'/')
        p = data.find(b'/' + skin_id + b'/' + skin_id + b'/')
    return data

def process_xml_file(file_path, user_id, run_hd):
    try:
        parser = ET.XMLParser(remove_blank_text=True)
        tree = ET.parse(file_path, parser)
        root = tree.getroot()
        if root.get("enabled") == "false":
            print(f"  [Bo qua ca file]: The goc co thuoc tinh enabled='false'")
            return
        mod0 = mod_11120_axbx(root, user_id, file_path)
        mod0b = mod_13210_addtrack(root, user_id, file_path)
        mod0c = mod_13213_addtrack(root, user_id, file_path)
        mod0d = mod_106xx(root, user_id, file_path)
        mod1 = mod_binh_thuong(root, user_id, os.path.basename(file_path))
        mod2 = mod_dac_biet_1(root, user_id, os.path.basename(file_path))
        mod3 = mod_dac_biet_2(root, user_id, os.path.basename(file_path))
        mod4 = False
        if run_hd:
            mod4 = mod_tich_hop_hd(root) if not (user_id == '13213' and os.path.basename(file_path) == 'S1B1.xml') else False
        mod5 = mod_dac_biet_15009_15015(root, user_id, file_path)
        if any([mod0, mod0b, mod0c, mod0d, mod1, mod2, mod3, mod4, mod5]):
            tree.write(file_path, pretty_print=True, xml_declaration=True, encoding="utf-8")
        else:
            pass
    except Exception as e:
        pass

def pack_hero_actions(output_hero_base, hero_name):
    prefix = hero_name[:3]
    skill_dir = os.path.join(output_hero_base, hero_name, 'skill')
    if not os.path.isdir(skill_dir):
        return None
    pkg_name = f'Actor_{prefix}_Actions.pkg.bytes'
    pkg_path = os.path.join(output_hero_base, pkg_name)
    with zipfile.ZipFile(pkg_path, 'w', zipfile.ZIP_STORED) as zipf:
        for root_dir, _, files in os.walk(skill_dir):
            for file in files:
                fpath = os.path.join(root_dir, file)
                rel = os.path.relpath(fpath, start=output_hero_base)
                zipf.write(fpath, rel)
    return pkg_path

def pack_hero_infos(output_base, hero_name, ids=None, hd=False, zd=None):
    prefix = hero_name[:3]
    out_prefab = f'{output_base}/Resources/1.62.1/Prefab_Characters'
    prefab_dir = f'{out_prefab}/Prefab_Hero/{hero_name}'
    pkg_name = f'Actor_{prefix}_Infos.pkg.bytes'
    pkg_path = f'{out_prefab}/{pkg_name}'
    os.makedirs(os.path.dirname(pkg_path), exist_ok=True)
    # Check if this hero needs pet handling (137 or 526)
    need_pet = (prefix in ('137', '526'))
    if need_pet and ids:
        skinid = None
        for sid in ids:
            if sid[:3] == prefix:
                skinid = sid.encode()
                break
        if skinid:
            # Create pet directories
            decompress = hero_name
            os.makedirs(f'{out_prefab}/{decompress}', exist_ok=True)
            os.makedirs(f'{out_prefab}/{decompress}_pet', exist_ok=True)
            # Copy pet actorinfo
            pet_src = f'./KIANA_AOV/Resources/1.62.1/Prefab_Characters/Prefab_Pet/{decompress}_Pet/{decompress}_Pet_actorinfo.bytes'
            pet_dst = f'{out_prefab}/{decompress}_pet/{decompress}_Pet_actorinfo.bytes'
            if os.path.exists(pet_src):
                with open(pet_src, 'rb') as f:
                    a = f.read()
                if prefix == '526':
                    a = decompress_(a, zd) if (hd and b'\x28\xb5\x2f\xfd' in a) else a
                    t = str(int(skinid[3:].decode())+1).encode('utf-8')
                    if len(t) == 1:
                        for i in range(1, 10):
                            if str(i).encode('utf-8') != t:
                                a = a.replace(skinid[:3]+str(i).encode('utf-8'), skinid[:3]+t)
                with open(pet_dst, 'wb') as f:
                    f.write(a)
            # Copy hero actorinfo to Prefab_Characters/{decompress}/
            hero_src = f'{prefab_dir}/{decompress}_actorinfo.bytes'
            if os.path.exists(hero_src):
                with open(hero_src, 'rb') as f:
                    a = f.read()
                with open(f'{out_prefab}/{decompress}/{decompress}_actorinfo.bytes', 'wb') as f:
                    f.write(a)
            # Zip both decompress and decompress_pet
            with zipfile.ZipFile(pkg_path, 'w', zipfile.ZIP_STORED) as zipf:
                for folder_name in [decompress, f'{decompress}_pet']:
                    folder_path = f'{out_prefab}/{folder_name}'
                    if os.path.isdir(folder_path):
                        for root_dir, _, files in os.walk(folder_path):
                            for file in files:
                                fpath = os.path.join(root_dir, file)
                                arcname = os.path.relpath(fpath, start=out_prefab)
                                zipf.write(fpath, arcname)
            # Cleanup
            for fname in os.listdir(out_prefab):
                fpath = os.path.join(out_prefab, fname)
                if os.path.isdir(fpath) and 'bytes' not in fname and fname != 'Prefab_Hero':
                    shutil.rmtree(fpath)
        else:
            need_pet = False
    if not need_pet:
        if not os.path.isdir(prefab_dir):
            return None
        with zipfile.ZipFile(pkg_path, 'w', zipfile.ZIP_STORED) as zipf:
            for root_dir, _, files in os.walk(prefab_dir):
                for file in files:
                    fpath = os.path.join(root_dir, file)
                    rel = os.path.relpath(fpath, start=f'{output_base}/Resources/1.62.1/')
                    zipf.write(fpath, rel)
    return pkg_path

def mod_sound_all(dst_base, ids, hd, zd):
    """Mod Sound files using soundpack.py logic for all IDs"""
    sound_path = f'{dst_base}/Databin/Client/Sound'
    if not os.path.isdir(sound_path):
        return False
    sound_files = [f for f in os.listdir(sound_path) if f.endswith('.bytes')]
    for ID in ids:
        all_id = []
        for id_num in range(21):
            id_str = f"{id_num:02d}"
            all_id.append(b"\x00" + int(ID[:3] + id_str).to_bytes(4, byteorder="little"))
        skinmd = all_id[0]
        skin = all_id[int(ID[3:])]
        other_ids = [x for x in all_id if x != skin and x != skinmd]
        for name in sound_files:
            sp = os.path.join(sound_path, name)
            with open(sp, 'rb') as f:
                A = f.read()
            if hd and b'\x28\xb5\x2f\xfd' in A:
                A = decompress_(A, zd)
            if name != "CoupleSound.bytes":
                for id_bytes in other_ids:
                    A = A.replace(id_bytes + b"\x00" * 8, b"\x0000" + b"\x00" * 10)
            else:
                for id_bytes in other_ids:
                    A = A.replace(id_bytes + b"\x02\x00\x00\x00\x01", b"\x0000\x00\x00\x02\x00\x00\x00\x01")
            if A.find(skin) != -1:
                if name != "CoupleSound.bytes":
                    A = A.replace(skinmd + b"\x00" * 8, b"\x0000" + b"\x00" * 10)
                    A = A.replace(skin + b"\x00" * 8, skinmd + b"\x00" * 8)
                else:
                    A = A.replace(skinmd + b"\x02\x00\x00\x00\x01", b"\x0000\x00\x00\x02\x00\x00\x00\x01")
                    A = A.replace(skin + b"\x02\x00\x00\x00\x01", skinmd + b"\x02\x00\x00\x00\x01")
            if hd:
                A = compress_(A, zd)
            with open(sp, 'wb') as f:
                f.write(A)
    return True

def mod_iconpack_all(dst_base, ids, hd, zd):
    """Mod heroSkin.bytes + HeroSkinShop.bytes using iconpack.py logic for all IDs"""
    file_names = ['Actor/heroSkin.bytes', 'Shop/HeroSkinShop.bytes']
    for ID in ids:
        IDB = int(ID).to_bytes(4, byteorder="little")
        IDH = int(ID[:3]).to_bytes(4, byteorder="little")
        for idx_f, rel_file in enumerate(file_names):
            fpath = f'{dst_base}/Databin/Client/{rel_file}'
            if not os.path.exists(fpath):
                continue
            with open(fpath, 'rb') as f:
                Code = f.read()
            if hd and b'\x28\xb5\x2f\xfd' in Code:
                Code = decompress_(Code, zd)
            All = []
            Skin = None
            Find = -10
            while True:
                Find = Code.find(b"\x00\x00" + IDH, Find + 10)
                if Find == -1:
                    break
                tid = Code[Find-2:Find]
                if len(tid) >= 2 and str(int.from_bytes(tid, byteorder="little"))[:3] == ID[:3]:
                    VT2 = int.from_bytes(Code[Find-6:Find-4], byteorder="little")
                    Code2 = Code[Find-6:Find-6+VT2]
                    All.append(Code2)
                    if Code2.find(IDB) != -1:
                        Skin = Code2
            if Skin is None:
                print(f"  [WARN] Khong tim thay Skin ID {ID} trong {rel_file}")
                continue
            is_heroskin = (idx_f == 0)
            for Id in All:
                Cache = Skin.replace(Skin[4:6], Id[4:6], 1)
                Cache = Cache.replace(Cache[35:44], Id[35:40] + Cache[40:44], 1)
                Hero = hex(int(ID[:3]))[2:]
                if len(Hero) == 3:
                    Hero = Hero[1:3] + "0" + Hero[0]
                else:
                    Hero += "00"
                Hero += "0000"
                Hero = bytes.fromhex(Hero)
                Cache = Cache.replace(Cache[8:12], Hero, 1)
                if is_heroskin and Id == All[0]:
                    ID30 = b"\x07\x00\x00\x0030" + bytes(ID[:3] + "0", "utf8") + b"\x00"
                    XYZ = Cache[64]
                    ID0 = Cache[64:68+XYZ]
                    Cache = Cache.replace(ID0, ID30, 1)
                    vt = Id.find(b"Hero_")
                    if vt != -1:
                        NumHero = Id[vt-4]
                        Hero_bytes = Id[vt-4:vt+NumHero]
                        Cache = Cache.replace(b"jpg\x00\x01\x00\x00\x00\x00", b"jpg\x00" + Hero_bytes, 1)
                        Full = Cache.count(Hero_bytes)
                        if Full > 1:
                            Cache = Cache.replace(b"jpg\x00" + Hero_bytes, b"jpg\x00\x01\x00\x00\x00\x00", Full - 1)
                        EndTheCode = hex(len(Cache))
                        if len(EndTheCode) == 5:
                            EndTheCode = EndTheCode[3:5] + "0" + EndTheCode[2:3]
                        else:
                            EndTheCode = EndTheCode[4:6] + EndTheCode[2:4]
                        EndTheCode = bytes.fromhex(EndTheCode)
                        Cache = Cache.replace(Cache[0:2], EndTheCode, 1)
                Code = Code.replace(Id, Cache, 1)
            if hd:
                Code = compress_(Code, zd)
            with open(fpath, 'wb') as f:
                f.write(Code)
    return True

def mod_skill_all(dst_base, ids, hd, zd):
    """Mod liteBulletCfg.bytes + skillmark.bytes using AutoSkill.py logic for all IDs"""
    files = [
        f'{dst_base}/Databin/Client/Skill/liteBulletCfg.bytes',
        f'{dst_base}/Databin/Client/Skill/skillmark.bytes',
    ]
    for ID in ids:
        IDS = bytes(f"fects/{ID[:3]}_", "utf8")
        for fpath in files:
            if not os.path.exists(fpath):
                continue
            with open(fpath, 'rb') as f:
                CodeAll = f.read()
            if hd and b'\x28\xb5\x2f\xfd' in CodeAll:
                CodeAll = decompress_(CodeAll, zd)
            acode = []
            bcode = []
            pos = 140
            while pos + 2 <= len(CodeAll):
                SL = CodeAll[pos:pos+2]
                rec_len = SL[0] + SL[1] * 256 + 4
                if pos + rec_len > len(CodeAll):
                    break
                Code = CodeAll[pos:pos+rec_len]
                if IDS in Code:
                    acode.append(Code)
                pos += rec_len
            if not acode:
                continue
            for code in acode:
                vt1 = code.find(IDS) + 6
                vt2 = code.find(b"/", vt1) + 1
                name_hero = code[vt1:vt2]
                code = code.replace(b"Prefab_Skill_Effects/Hero_Skill_Effects", b"prefab_skill_effects/hero_skill_effects")
                code = code.replace(b"hero_skill_effects/"+name_hero, b"hero_skill_effects/"+name_hero+bytes(ID+"/","utf"))
                vtm = code.find(b"prefab_skill_effects") - 4
                newlen = code[vtm] + len(ID) + 1
                gt = newlen.to_bytes(1, 'little') + b"\x00" * 3
                code = code.replace(code[vtm:vtm+4], gt)
                newval = len(code) - 4
                tgt = newval.to_bytes(2, 'little')
                code = code.replace(code[0:2], tgt, 1)
                bcode.append(code)
            for ty in range(len(acode)):
                CodeAll = CodeAll.replace(acode[ty], bcode[ty], 1)
            if hd:
                CodeAll = compress_(CodeAll, zd)
            with open(fpath, 'wb') as f:
                f.write(CodeAll)
    return True

def mod_motion_all(dst_res_base, ids):
    """Mod ResSkinMotionBaseCfg.bytes: read from File_mod (already decompressed), mod all IDs"""
    dst_mot = f'{dst_res_base}/Databin/Client/Motion/ResSkinMotionBaseCfg.bytes'
    if not os.path.exists(dst_mot):
        print("  [That bai] Khong tim thay ResSkinMotionBaseCfg.bytes trong File_mod")
        return False
    with open(dst_mot, 'rb') as f:
        strin = f.read()
    modified = False
    for uid in ids:
        prefix3 = uid[:3]
        ID = uid
        List = []
        for i in range(30):
            List.append(dec_to_hex(int(prefix3 + f'{i:02d}')))
        main = strin[140:]
        List_code = []
        while True:
            if len(main) < 2:
                break
            id2 = main[:2]
            rec_len = hex_to_dec(id2) + 4
            if rec_len > len(main):
                break
            entry = main[:rec_len]
            if dec_to_hex(int(ID)) + b'\x00\x00' in entry:
                List_code.append(entry)
            for hid in List:
                if hid + b'\x00\x00' in entry and hid + b'\x00\x00' != dec_to_hex(int(ID)) + b'\x00\x00':
                    List_code.append(entry)
                else:
                    break
            main = main[rec_len:]
            if main == b'':
                break
        if not List_code:
            continue
        code_special = []
        code_normal_1 = []
        for code in List_code:
            if code[:2] in [b'6\x00', b'S\x00']:
                code_special.append(code)
            else:
                code_normal_1.append(code)
        code_normal_2 = []
        if code_special:
            idcode = b'\x00\x00' + code_special[0][21:25]
            for code in code_normal_1:
                for hid in List:
                    p = code.find(hid + b'\x00\x00')
                    if p != -1:
                        code = code.replace(code[p:p+8], hid + idcode, 1)
                code_normal_2.append(code)
        else:
            for code in code_normal_1:
                p = code.find(dec_to_hex(int(ID)) + b'\x00\x00')
                if p != -1:
                    idcode = code[p+2:p+8]
                    for hid in List:
                        p = code.find(hid + b'\x00\x00')
                        if p != -1:
                            code = code.replace(code[p:p+8], hid + idcode, 1)
                code_normal_2.append(code)
        for i in range(len(code_normal_1)):
            if len(code_normal_1) == len(code_normal_2):
                strin = strin.replace(code_normal_1[i], code_normal_2[i], 1)
        if len(code_special) + len(code_normal_1) == 0:
            for hid in List:
                strin = strin.replace(hid + b'\x00\x00', b'00\x00\x00', 1)
        modified = True
    if not modified:
        print("  [That bai] Khong co ID nao mod duoc Motion")
        return False
    with open(dst_mot, 'wb') as f:
        f.write(strin)
    return True

# ---- Back.xml functions (merged from back.py) ----
def back_new_guid():
    return str(uuid.uuid4())

def back_parse_single_ids(text):
    pairs = []
    for token in text.split():
        try:
            main_id = int(token)
        except:
            print("⚠ ID không hợp lệ:", token)
            continue
        prefix = str(main_id)[:3]
        others = []
        for i in range(0, 21):
            sub_id = int(prefix + f"{i:02d}")
            if sub_id != main_id:
                others.append(sub_id)
        pairs.append((main_id, others))
    return pairs

def back_find_fodder(folder_path, prefix3):
    prefix3 = str(prefix3)
    for name in os.listdir(folder_path):
        if name.startswith(prefix3 + "_"):
            return name
    return None

def back_find_existing_tracks(root, target_id):
    found_tracks = []
    for track in root.findall(".//Track"):
        for node in track.findall("SkinOrAvatarList"):
            if node.get("id") == str(target_id):
                found_tracks.append(track)
                break
    return found_tracks

def back_add_ids_to_track(track, ids_to_add):
    current_ids = set()
    for node in track.findall("SkinOrAvatarList"):
        current_ids.add(node.get("id"))
    added = 0
    for sid in ids_to_add:
        if str(sid) not in current_ids:
            ET.SubElement(track, "SkinOrAvatarList", {"id": str(sid)})
            added += 1
    return added

def back_create_tick(fodder, last_id, skin_ids):
    track = ET.Element("Track", {"trackName": "Mod_by_ytb_KIANAMODAOV","eventType": "TriggerParticleTick","guid": back_new_guid(),"enabled": "true","useRefParam": "false","refParamName": "","r": "0.000","g": "0.000","b": "0.000","execOnForceStopped": "false","execOnActionCompleted": "false","stopAfterLastEvent": "true","SkinAvatarFilterType": "9"})
    ev = ET.SubElement(track, "Event", {"eventName": "TriggerParticleTick","time": "7.000","isDuration": "false","guid": back_new_guid()})
    ET.SubElement(ev, "TemplateObject", {"name": "targetId","objectName": "None","id": "-1","isTemp": "false","refParamName": "","useRefParam": "false"})
    ET.SubElement(ev, "TemplateObject", {"name": "objectSpaceId","objectName": "self","id": "0","isTemp": "false","refParamName": "","useRefParam": "false"})
    ET.SubElement(ev, "String", {"name": "parentResourceName","value": "born_back_reborn/huijidi_01","useRefParam": "false"})
    ET.SubElement(ev, "String", {"name": "resourceName","value": f"prefab_skill_effects/hero_skill_effects/{fodder}/{last_id}/huijidi_01.Prefab","useRefParam": "true"})
    for sid in skin_ids:
        ET.SubElement(track, "SkinOrAvatarList", {"id": str(sid)})
    return track

def back_create_particle(fodder, last_id, skin_ids):
    track = ET.Element("Track", {"trackName": "Kiana_Mod_AOV","eventType": "TriggerParticle","guid": back_new_guid(),"enabled": "true","useRefParam": "false","refParamName": "","r": "0.000","g": "0.000","b": "0.000","execOnForceStopped": "false","execOnActionCompleted": "false","stopAfterLastEvent": "true","SkinAvatarFilterType": "9"})
    ev = ET.SubElement(track, "Event", {"eventName": "TriggerParticle","time": "0.000","length": "7.000","isDuration": "true","guid": back_new_guid()})
    ET.SubElement(ev, "TemplateObject", {"name": "targetId","objectName": "self","id": "0","isTemp": "false","refParamName": "","useRefParam": "false"})
    ET.SubElement(ev, "TemplateObject", {"name": "objectSpaceId","objectName": "self","id": "0","isTemp": "false","refParamName": "","useRefParam": "false"})
    ET.SubElement(ev, "String", {"name": "parentResourceName","value": "prefab_skill_effects/tongyong_effects/tongyong_hurt/born_back_reborn/huicheng_tongyong_01","useRefParam": "false"})
    ET.SubElement(ev, "String", {"name": "resourceName","value": f"prefab_skill_effects/hero_skill_effects/{fodder}/{last_id}/huicheng_tongyong_01.Prefab","useRefParam": "true"})
    for sid in skin_ids:
        ET.SubElement(track, "SkinOrAvatarList", {"id": str(sid)})
    return track

def back_create_hit_trigger():
    track = ET.Element("Track", {"trackName": "Mod_by_Youtuber_Kiana_Mod_AOV","eventType": "HitTriggerTick","guid": "CAM_XA_Kiana_Mod","enabled": "true","useRefParam": "false","refParamName": "","r": "0.000","g": "0.000","b": "0.000","execOnForceStopped": "false","execOnActionCompleted": "false","stopAfterLastEvent": "true"})
    ev = ET.SubElement(track, "Event", {"eventName": "HitTriggerTick","time": "0.000","isDuration": "false","guid": "https://youtube.com/@kianamodaov?si=J_d_gSoJ4u53VQru"})
    ET.SubElement(ev, "TemplateObject", {"name": "targetId","id": "0","objectName": "self","isTemp": "false","refParamName": "","useRefParam": "false"})
    ET.SubElement(ev, "TemplateObject", {"name": "hitTargetId","id": "0","objectName": "self","isTemp": "false","refParamName": "","useRefParam": "false"})
    ET.SubElement(ev, "int", {"name": "SelfSkillCombineID_1","value": "530510","refParamName": "","useRefParam": "false"})
    ET.SubElement(ev, "TemplateObject", {"name": "triggerId","id": "-1","objectName": "None","isTemp": "false","refParamName": "","useRefParam": "false"})
    return track

def back_process_back(back_xml, output_xml, folder_path, pairs):
    tree = ET.parse(back_xml)
    root = tree.getroot()
    action = root.find(".//Action")
    if action is None:
        print("❌ Không tìm thấy <Action>")
        return
    pos = len(list(action))
    has_new_tracks = False
    for last_id, others in pairs:
        prefix3 = str(last_id)[:3]
        skin_ids = [last_id] + others
        old_tracks = back_find_existing_tracks(root, last_id)
        if old_tracks:
            for tr in old_tracks:
                added = back_add_ids_to_track(tr, others)
        fodder = back_find_fodder(folder_path, prefix3)
        if not fodder:
            print("❌ Không có fodder:", prefix3)
            continue
        t1 = back_create_tick(fodder, last_id, skin_ids)
        t2 = back_create_particle(fodder, last_id, skin_ids)
        action.insert(pos, t1)
        pos += 1
        action.insert(pos, t2)
        pos += 1
        has_new_tracks = True
    if has_new_tracks:
        t3 = back_create_hit_trigger()
        action.insert(pos, t3)
        pos += 1
    tree.write(output_xml, encoding="utf-8", xml_declaration=True)

def mod_back_xml(src_base, dst_base, ids, hd, zd):
    src_path = f'{src_base}/commonresource/Back.xml'
    dst_dir = f'{dst_base}/commonresource'
    dst_path = f'{dst_dir}/Back.xml'
    if not os.path.exists(src_path):
        return False
    os.makedirs(dst_dir, exist_ok=True)
    if hd:
        with open(src_path, 'rb') as f:
            raw = decompress_(f.read(), zd)
        with open(dst_path, 'wb') as f:
            f.write(raw)
    else:
        shutil.copy2(src_path, dst_path)
    text = ' '.join(ids)
    pairs = back_parse_single_ids(text)
    folder_path = 'KIANA_AOV/Resources/1.62.1/Ages/Prefab_Characters/Prefab_Hero'
    back_process_back(dst_path, dst_path, folder_path, pairs)
    if hd:
        with open(dst_path, 'rb') as f:
            raw = f.read()
        with open(dst_path, 'wb') as f:
            f.write(compress_(raw, zd))
    return True

def pack_common_actions(output_base):
    common_dir = f'{output_base}/Resources/1.62.1/Ages/Prefab_Characters/Prefab_Hero'
    common_res_dirs = ['commonresource', 'KeySpell', 'PassiveResource', 'mowen', 'Ultrafire', 'SeasonPlay']
    pkg_path = os.path.join(common_dir, 'CommonActions.pkg.bytes')
    with zipfile.ZipFile(pkg_path, 'w', zipfile.ZIP_STORED) as zipf:
        for folder in common_res_dirs:
            src_dir = os.path.join(common_dir, folder)
            if os.path.isdir(src_dir):
                for root_dir, _, files in os.walk(src_dir):
                    for file in files:
                        fpath = os.path.join(root_dir, file)
                        arcname = os.path.join(folder, os.path.relpath(fpath, src_dir))
                        zipf.write(fpath, arcname)
    for folder in common_res_dirs:
        src_dir = os.path.join(common_dir, folder)
        if os.path.isdir(src_dir):
            shutil.rmtree(src_dir)
    return pkg_path

def read_ids_from_list(list_path='list_mod.txt'):
    if not os.path.exists(list_path):
        return None
    ids = []
    with open(list_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if any(kw in line.lower() for kw in ['hd', 'rov', 'mayyeu', 'uid']):
                continue
            ids.append(line)
    return ids if ids else None

def main():
    print("=========================================")
    print("     TOOL AUTO MOD SKIN LQ ")
    print("=========================================")
    ids = read_ids_from_list()
    if not ids:
        print("Khong tim thay ID nao trong list_mod.txt (cung thu muc)!")
        print("Vui long tao file list_mod.txt voi moi ID tren mot dong.")
        return
    run_hd = True
    source_base = 'KIANA_AOV/Resources/1.62.1/Ages/Prefab_Characters/Prefab_Hero'
    output_base = 'File_mod'
    output_hero_base = f'{output_base}/Resources/1.62.1/Ages/Prefab_Characters/Prefab_Hero'
    os.makedirs(output_hero_base, exist_ok=True)
    print(f"Tim thay {len(ids)} ID can xu ly.")
    res_base = 'KIANA_AOV/Resources/1.62.1'
    out_base = f'{output_base}/Resources/1.62.1'
    giai_nen_file_zip()
    print("[1/7] Dang mod hiệu ứng...")
    process_common_resources(f'{res_base}/Ages/Prefab_Characters/Prefab_Hero', f'{out_base}/Ages/Prefab_Characters/Prefab_Hero', run_hd, _ZSTD_DICT)
    print("  Xong hiệu ứng!")
    print("[2/7] Dang mod biến về...")
    mod_back_xml(f'{res_base}/Ages/Prefab_Characters/Prefab_Hero', f'{out_base}/Ages/Prefab_Characters/Prefab_Hero', ids, run_hd, _ZSTD_DICT)
    print("  Xong Back.xml!")
    print("[3/7] Dang mod Databin...")
    process_databin(f'{res_base}/Databin/Client', f'{out_base}/Databin/Client', run_hd, _ZSTD_DICT)
    print("  Xong Databin!")
    print(f"\n[4/7] Dang mod {len(ids)} hero(s)...")
    processed_heroes = []
    nh_processed = set()
    for uid in ids:
        hero_folder = None
        prefix3 = uid[:3]
        if os.path.isdir(source_base):
            for item in os.listdir(source_base):
                if item.startswith(prefix3 + '_'):
                    hero_folder = item
                    break
        if not hero_folder:
            continue
        src_skill = os.path.join(source_base, hero_folder, 'skill')
        if not os.path.isdir(src_skill):
            continue
        dst_hero = os.path.join(output_hero_base, hero_folder)
        dst_skill = os.path.join(dst_hero, 'skill')
        os.makedirs(dst_skill, exist_ok=True)
        xml_files = [f for f in os.listdir(src_skill) if f.lower().endswith('.xml')]
        if not xml_files:
            continue
        has_modified = False
        for xml_file in xml_files:
            src_path = os.path.join(src_skill, xml_file)
            dst_path = os.path.join(dst_skill, xml_file)
            xml_data = None
            try:
                if run_hd:
                    with open(src_path, 'rb') as f:
                        raw_data = f.read()
                    xml_data = decompress_(raw_data, _ZSTD_DICT)
                    tree = ET.parse(io.BytesIO(xml_data))
                    root = tree.getroot()
                    if root.get("enabled") == "false":
                        xml_data = fix_ef(xml_data, uid.encode())
                        with open(dst_path, 'wb') as f:
                            f.write(compress_(xml_data, _ZSTD_DICT))
                        continue
                    mod0 = mod_11120_axbx(root, uid, xml_file)
                    mod0b = mod_13210_addtrack(root, uid, xml_file)
                    mod0c = mod_13213_addtrack(root, uid, xml_file)
                    mod0d = mod_106xx(root, uid, xml_file)
                    mod1 = mod_binh_thuong(root, uid, xml_file)
                    mod2 = mod_dac_biet_1(root, uid, xml_file)
                    mod3 = mod_dac_biet_2(root, uid, xml_file)
                    mod4 = mod_tich_hop_hd(root) if not (uid == '13213' and xml_file == 'S1B1.xml') else False
                    mod5 = mod_dac_biet_15009_15015(root, uid, xml_file)
                    if any([mod0, mod0b, mod0c, mod0d, mod1, mod2, mod3, mod4, mod5]):
                        xml_out = ET.tostring(tree, pretty_print=True, xml_declaration=True, encoding="utf-8")
                        xml_out = fix_ef(xml_out, uid.encode())
                        with open(dst_path, 'wb') as f:
                            f.write(compress_(xml_out, _ZSTD_DICT))
                        has_modified = True
                    else:
                        xml_data = fix_ef(xml_data, uid.encode())
                        with open(dst_path, 'wb') as f:
                            f.write(compress_(xml_data, _ZSTD_DICT))
                else:
                    shutil.copy2(src_path, dst_path)
                    process_xml_file(dst_path, uid, run_hd)
                    with open(dst_path, 'rb') as f:
                        raw = f.read()
                    raw = fix_ef(raw, uid.encode())
                    with open(dst_path, 'wb') as f:
                        f.write(raw)
                    has_modified = True
            except Exception as e:
                if run_hd and xml_data is not None:
                    xml_data = fix_ef(xml_data, uid.encode())
                    with open(dst_path, 'wb') as f:
                        f.write(compress_(xml_data, _ZSTD_DICT))
                elif run_hd:
                    shutil.copy2(src_path, dst_path)
                else:
                    shutil.copy2(src_path, dst_path)
        if has_modified:
            processed_heroes.append(hero_folder)
        nh_result, nh_list = process_ngoai_hinh(uid, hero_folder, run_hd, _ZSTD_DICT)
        if nh_result:
            nh_processed.add(hero_folder)
    print("  Xong heroes!")
    print("[5/7] Dang mod dieu nhay...")
    mod_motion_all(out_base, ids)
    print("  Xong dieu nhay!")
    print("[6/7] Dang mod (Icon, Sound, Skill)...")
    mod_iconpack_all(out_base, ids, run_hd, _ZSTD_DICT)
    mod_sound_all(out_base, ids, run_hd, _ZSTD_DICT)
    mod_skill_all(out_base, ids, run_hd, _ZSTD_DICT)
    print("  Xong !")
    print("[7/7] Dang tao danh sach skin...")
    skin_name_list = []
    for uid in ids:
        try:
            _, skin_name, _ = ten_skin_hieu_ung(int(uid))
            if skin_name and skin_name.strip():
                skin_name_list.append(skin_name.strip())
            else:
                skin_name_list.append(uid)
        except:
            skin_name_list.append(uid)
    skin_list_path = os.path.join(output_base, 'danhsachskin.txt')
    with open(skin_list_path, 'w', encoding='utf-8') as f:
        for i, name in enumerate(skin_name_list, 1):
            f.write(f"{i}. {name}\n")
    print(f"  Xong danh sach skin!")
    print("\n=========================================")
    print("=== LOADING! ===")
    print("=========================================")
    if processed_heroes:
        for hero_name in processed_heroes:
            pack_hero_actions(output_hero_base, hero_name)
            hero_skill_path = os.path.join(output_hero_base, hero_name, 'skill')
            if os.path.isdir(hero_skill_path):
                shutil.rmtree(os.path.join(output_hero_base, hero_name))
    if nh_processed:
        for hero_name in nh_processed:
            pack_hero_infos(output_base, hero_name, ids, run_hd, _ZSTD_DICT)
            prefab_hero_dir = f'{output_base}/Resources/1.62.1/Prefab_Characters/Prefab_Hero/{hero_name}'
            if os.path.isdir(prefab_hero_dir):
                shutil.rmtree(prefab_hero_dir)
    if processed_heroes:
        pack_common_actions(output_base)
    print("\n=========================================")
    print("=== DA XONG TAT CA! ===")
    print("=========================================")
    print("  - Bien ve, Hieu ung, Icon, Bac, Am thanh")
    print("  - Nhieu nhay, An danh thuong, Ngoai hinh")
    folder_name = input("\nNhap ten thu muc de luu mod (trong File_mod): ").strip()
    if folder_name:
        dst = os.path.join(output_base, folder_name)
        os.makedirs(dst, exist_ok=True)
        src_res = os.path.join(output_base, 'Resources')
        if os.path.isdir(src_res):
            shutil.move(src_res, os.path.join(dst, 'Resources'))
        src_skin = os.path.join(output_base, 'danhsachskin.txt')
        if os.path.exists(src_skin):
            shutil.move(src_skin, os.path.join(dst, 'danhsachskin.txt'))
        print(f"  Da luu vao: File_mod/{folder_name}/")
    else:
        print(f"  Khong nhap ten. Mod nam trong: {output_base}/")

def giai_nen_file_zip():
    print('------ DANG GIAI NEN AGES VA PREFAB_CHARACTER ... ------')
    def giai_nen(z, a):
        fantasy_zip = zipfile.ZipFile(z + a)
        fantasy_zip.extractall(z)
        return f'Giai Nen Xong File: {a}'

    ver = '1.62.1'
    t1 = f'./KIANA_AOV/Resources/{ver}/Ages/Prefab_Characters/Prefab_Hero/'
    t2 = f'./KIANA_AOV/Resources/{ver}/Prefab_Characters/'
    if not os.path.isdir(f'./KIANA_AOV/Resources/{ver}/Ages/Prefab_Characters/Prefab_Hero/150_HanXin'):
        for file in os.listdir(t2):
            if 'Actor' in file:
                print(giai_nen(t2, file), end='\r')
        for file in os.listdir(t1):
            if 'Rapid' not in file and 'Newbie' not in file and 'Actor' in file:
                print(giai_nen(t1, file), end='\r')
            if file == 'CommonActions.pkg.bytes':
                print(giai_nen(t1, file), end='\r')
        print(giai_nen(f'./KIANA_AOV/Resources/{ver}/Ages/', 'Prefab_Gear.pkg.bytes'), end='\r')
    print('--------------- DA GIAI NEN XONG ROI DO ----------------')

if __name__ == "__main__":
    main()
