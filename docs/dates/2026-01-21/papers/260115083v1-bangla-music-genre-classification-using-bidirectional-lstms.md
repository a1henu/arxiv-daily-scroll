---
layout: default
title: Bangla Music Genre Classification Using Bidirectional LSTMS
---

# Bangla Music Genre Classification Using Bidirectional LSTMS
**arXiv**：[2601.15083v1](https://arxiv.org/abs/2601.15083) · [PDF](https://arxiv.org/pdf/2601.15083.pdf)  
**作者**：Muntakimur Rahaman, Md Mahmudul Hoque, Md Mehedi Hassain  

**一句话要点**：提出基于双向LSTM的孟加拉音乐流派分类方法，以提升大规模音乐库的检索效率。

**关键词**：音乐流派分类, 双向LSTM, MFCC特征提取, 孟加拉音乐, 音频分类, 深度学习

## 3 点简述
- 核心问题：孟加拉音乐流派自动分类，以应对数字音乐激增带来的索引和检索挑战。
- 方法要点：使用MFCC特征提取和双向LSTM网络，构建音频分类模型。
- 实验或效果：在自建十类孟加拉音乐数据集上，实现78%的分类准确率。

## 摘要（原文）

> Bangla music is enrich in its own music cultures. Now a days music genre classification is very significant because of the exponential increase in available music, both in digital and physical formats. It is necessary to index them accordingly to facilitate improved retrieval. Automatically classifying Bangla music by genre is essential for efficiently locating specific pieces within a vast and diverse music library. Prevailing methods for genre classification predominantly employ conventional machine learning or deep learning approaches. This work introduces a novel music dataset comprising ten distinct genres of Bangla music. For the task of audio classification, we utilize a recurrent neural network (RNN) architecture. Specifically, a Long Short-Term Memory (LSTM) network is implemented to train the model and perform the classification. Feature extraction represents a foundational stage in audio data processing. This study utilizes Mel-Frequency Cepstral Coefficients (MFCCs) to transform raw audio waveforms into a compact and representative set of features. The proposed framework facilitates music genre classification by leveraging these extracted features. Experimental results demonstrate a classification accuracy of 78%, indicating the system's strong potential to enhance and streamline the organization of Bangla music genres.

