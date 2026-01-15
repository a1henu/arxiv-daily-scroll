---
layout: default
title: Towards Realistic Synthetic Data for Automatic Drum Transcription
---

# Towards Realistic Synthetic Data for Automatic Drum Transcription
**arXiv**：[2601.09520v1](https://arxiv.org/abs/2601.09520) · [PDF](https://arxiv.org/pdf/2601.09520.pdf)  
**作者**：Pierfrancesco Melucci, Paolo Merialdo, Taketo Akama  

**一句话要点**：提出半监督方法自动构建高质量鼓样本库，用于合成数据训练自动鼓转录模型。

**关键词**：自动鼓转录, 合成数据生成, 半监督学习, 序列到序列模型, 音频处理

## 3 点简述
- 核心问题：自动鼓转录依赖稀缺的配对音频-MIDI数据，现有合成数据存在领域差距。
- 方法要点：从无标签音频自动收集多样鼓样本，合成高质量数据集训练序列到序列模型。
- 实验或效果：在ENST和MDB测试集上达到新最优结果，优于全监督和先前合成方法。

## 摘要（原文）

> Deep learning models define the state-of-the-art in Automatic Drum Transcription (ADT), yet their performance is contingent upon large-scale, paired audio-MIDI datasets, which are scarce. Existing workarounds that use synthetic data often introduce a significant domain gap, as they typically rely on low-fidelity SoundFont libraries that lack acoustic diversity. While high-quality one-shot samples offer a better alternative, they are not available in a standardized, large-scale format suitable for training. This paper introduces a new paradigm for ADT that circumvents the need for paired audio-MIDI training data. Our primary contribution is a semi-supervised method to automatically curate a large and diverse corpus of one-shot drum samples from unlabeled audio sources. We then use this corpus to synthesize a high-quality dataset from MIDI files alone, which we use to train a sequence-to-sequence transcription model. We evaluate our model on the ENST and MDB test sets, where it achieves new state-of-the-art results, significantly outperforming both fully supervised methods and previous synthetic-data approaches. The code for reproducing our experiments is publicly available at https://github.com/pier-maker92/ADT_STR

