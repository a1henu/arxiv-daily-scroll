---
layout: default
title: Fun-Audio-Chat Technical Report
---

# Fun-Audio-Chat Technical Report
**arXiv**：[2512.20156v1](https://arxiv.org/abs/2512.20156) · [PDF](https://arxiv.org/pdf/2512.20156.pdf)  
**作者**：Qian Chen, Luyao Cheng, Chong Deng, Xiangang Li, Jiaqing Liu, Chao-Hong Tan, Wen Wang, Junhao Xu, Jieping Ye, Qinglin Zhang, Qiquan Zhang, Jingren Zhou  

**一句话要点**：提出Fun-Audio-Chat大型音频语言模型，通过双分辨率语音表示和核心鸡尾酒训练解决语音-文本模型中的语义稀释和灾难性遗忘问题。

**关键词**：大型音频语言模型, 双分辨率语音表示, 核心鸡尾酒训练, 多任务DPO训练, 语音-文本联合建模, 灾难性遗忘缓解

## 3 点简述
- 核心问题：现有联合语音-文本模型面临语音与文本令牌频率不匹配导致的语义信息稀释、高计算成本和灾难性遗忘。
- 方法要点：采用双分辨率语音表示平衡效率与质量，结合核心鸡尾酒训练和多任务DPO训练以保留文本LLM知识并增强音频能力。
- 实验或效果：在语音转文本和语音转语音任务中表现优异，在口语问答基准上排名前列，并开源8B模型和代码。

## 摘要（原文）

> Recent advancements in joint speech-text models show great potential for seamless voice interactions. However, existing models face critical challenges: temporal resolution mismatch between speech tokens (25Hz) and text tokens (~3Hz) dilutes semantic information, incurs high computational costs, and causes catastrophic forgetting of text LLM knowledge. We introduce Fun-Audio-Chat, a Large Audio Language Model addressing these limitations via two innovations from our previous work DrVoice. First, Dual-Resolution Speech Representations (DRSR): the Shared LLM processes audio at efficient 5Hz (via token grouping), while the Speech Refined Head generates high-quality tokens at 25Hz, balancing efficiency (~50% GPU reduction) and quality. Second, Core-Cocktail Training, a two-stage fine-tuning with intermediate merging that mitigates catastrophic forgetting. We then apply Multi-Task DPO Training to enhance robustness, audio understanding, instruction-following and voice empathy. This multi-stage post-training enables Fun-Audio-Chat to retain text LLM knowledge while gaining powerful audio understanding, reasoning, and generation. Unlike recent LALMs requiring large-scale audio-text pre-training, Fun-Audio-Chat leverages pre-trained models and extensive post-training. Fun-Audio-Chat 8B and MoE 30B-A3B achieve competitive performance on Speech-to-Text and Speech-to-Speech tasks, ranking top among similar-scale models on Spoken QA benchmarks. They also achieve competitive to superior performance on Audio Understanding, Speech Function Calling, Instruction-Following and Voice Empathy. We develop Fun-Audio-Chat-Duplex, a full-duplex variant with strong performance on Spoken QA and full-duplex interactions. We open-source Fun-Audio-Chat-8B with training and inference code, and provide an interactive demo.

