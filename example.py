import mido

length = 8

pitch_list = [[] for t0 in range(length)]  # 每个半拍所有音符的音高
vel_list = [[] for t1 in range(length)]  # 每个半拍所有音符的音量

# 确定每个半拍的音量和音高
for i in range(length):
    note_num = 3
    while True:
        pitch_list[i] = [t2 * 10 + i + 50 for t2 in range(note_num)]
        vel_list[i] = [t3 * 10 + i + 50 for t3 in range(note_num)]
        if len(pitch_list[i]) == len(set(pitch_list[i])):  # 同一时间音符的音高不能重合
            break

mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)

track.append(mido.MetaMessage('set_tempo', tempo=500000, time=0))
track.append(mido.MetaMessage('track_name', name='Piano 1', time=0))
track.append(mido.Message('program_change', program=1, time=0))  # 这个音轨使用的乐器

current_beat = 0
for i in range(length):
    for note, vel in zip(pitch_list[i], vel_list[i]):
        track.append(mido.Message('note_on', note=note, velocity=vel, time=150))
    for note, vel in zip(pitch_list[i], vel_list[i]):
        track.append(mido.Message('note_off', note=note, velocity=vel, time=50))

mid.save('framework.mid')
