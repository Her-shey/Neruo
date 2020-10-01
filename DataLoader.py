# data loader
import numpy as np

import os
import scipy.io
class MEGLoader():
    def __init__(self,data_path='./R0558/'):
        # one mat file with 24 records;
        # each record has 157 channels and 6000 frames
        # the 157*144000
        # self.dataset = np.load(data_path, allow_pickle=True)
    # data_path = './R0558/'
    # random noise combined with music
    # 
        self.Song_map = {'matdata165.mat':'abc', 'matdata166.mat':'star','matdata167.mat':'esty','matdata168.mat':'ball'}
        self.datalist = None
        self.songlist = None
        self.song_start = 2000
        self.song_interval = 6000
        self.iter_number = 24
        self.current_index = 0
        temp_datalist = []
        temp_songlist = []
        for filename in self.Song_map.keys():
            if ".mat" in filename:
                
                data = scipy.io.loadmat(data_path+filename)['epoch']
                print('data shape:',data.shape,(144000,157))

                song = self.Song_map[filename]
                for ind in range(self.iter_number):
                    # temp_pair = [data[ind*self.song_interval+self.song_start:ind*self.song_interval+self.song_interval], song]
                    temp_datalist.append(data[ind*self.song_interval+self.song_start:ind*self.song_interval+self.song_interval])
                    temp_songlist.append(song)
        self.datalist = np.array(temp_datalist)
        self.songlist = np.array(temp_songlist)
        
    def chunking(self):
        pass

    def get_len(self):
        return len(self.datalist)


    def shuffle_samples(self):
        pass

    def get_batch(self, batch_size):
        if (self.current_index + batch_size) > self.get_len():
            # angumentation
            # self.iter_times+=1
            t = self.current_index
            self.current_index = 0
            # self.epoch += 1
            return self.datalist[t:], self.songlist[t:]
        else:
            t = self.current_index
            self.current_index += batch_size
            return self.datalist[
                t:self.current_index], self.songlist[t:self.current_index]
    def get_batch_by_ind(self,batch_size,ind):
      self.check()
      current_index = ind*batch_size
      if (current_index + batch_size) > self.get_n_sample():
          t = current_index
          current_index = 0
          #epoch += 1
          return self.datalist[t:], self.songlist[t:]
          
      else:
          t = current_index
          current_index += batch_size
          return self.datalist[
                t:self.current_index], self.songlist[t:self.current_index]    
