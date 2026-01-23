---
layout: default
title: Pay (Cross) Attention to the Melody: Curriculum Masking for Single-Encoder Melodic Harmonization
---

# Pay (Cross) Attention to the Melody: Curriculum Masking for Single-Encoder Melodic Harmonization
**arXiv**：[2601.16150v1](https://arxiv.org/abs/2601.16150) · [PDF](https://arxiv.org/pdf/2601.16150.pdf)  
**作者**：Maximos Kaliakatsos-Papakostas, Dimos Makris, Konstantinos Soiledis, Konstantinos-Theodoros Tsamis, Vassilis Katsouros, Emilios Cambouropoulos  

**一句话要点**：提出全到全训练课程以增强单编码器旋律和声化中的旋律-和声交互

**关键词**：旋律和声化, 单编码器Transformer, 训练课程, 掩码序列建模, 旋律-和声交互, 域外评估

## 3 点简述
- 核心问题：现有单编码器Transformer在旋律和声化中旋律-和声注意力弱，导致旋律线索利用不足。
- 方法要点：引入FF训练课程，先全掩码和声令牌再逐步全解掩，以强化旋律-和声交互。
- 实验或效果：在HookTheory数据集和爵士标准曲上评估，FF课程在多数指标上优于基线，尤其在域外评估中表现突出。

## 摘要（原文）

> Melodic harmonization, the task of generating harmonic accompaniments for a given melody, remains a central challenge in computational music generation. Recent single encoder transformer approaches have framed harmonization as a masked sequence modeling problem, but existing training curricula inspired by discrete diffusion often result in weak (cross) attention between melody and harmony. This leads to limited exploitation of melodic cues, particularly in out-of-domain contexts. In this work, we introduce a training curriculum, FF (full-to-full), which keeps all harmony tokens masked for several training steps before progressively unmasking entire sequences during training to strengthen melody-harmony interactions. We systematically evaluate this approach against prior curricula across multiple experimental axes, including temporal quantization (quarter vs. sixteenth note), bar-level vs. time-signature conditioning, melody representation (full range vs. pitch class), and inference-time unmasking strategies. Models are trained on the HookTheory dataset and evaluated both in-domain and on a curated collection of jazz standards, using a comprehensive set of metrics that assess chord progression structure, harmony-melody alignment, and rhythmic coherence. Results demonstrate that the proposed FF curriculum consistently outperforms baselines in nearly all metrics, with particularly strong gains in out-of-domain evaluations where harmonic adaptability to novel melodic queues is crucial. We further find that quarter-note quantization, intertwining of bar tokens, and pitch-class melody representations are advantageous in the FF setting. Our findings highlight the importance of training curricula in enabling effective melody conditioning and suggest that full-to-full unmasking offers a robust strategy for single encoder harmonization.

