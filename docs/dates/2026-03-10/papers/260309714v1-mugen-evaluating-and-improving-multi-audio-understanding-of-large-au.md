---
layout: default
title: MUGEN: Evaluating and Improving Multi-audio Understanding of Large Audio-Language Models
---

# MUGEN: Evaluating and Improving Multi-audio Understanding of Large Audio-Language Models
**arXiv**：[2603.09714v1](https://arxiv.org/abs/2603.09714) · [PDF](https://arxiv.org/pdf/2603.09714.pdf)  
**作者**：Chih-Kai Yang, Yun-Shao Tsai, Yu-Kai Guo, Ping-Le Tsai, Yen-Ting Piao, Hung-Wei Chen, Ting-Lin Hsiao, Yun-Man Hsu, Ke-Han Lu, Hung-yi Lee  

**一句话要点**：提出MUGEN基准以评估和改进大型音频-语言模型的多音频理解能力

**关键词**：多音频理解, 大型音频-语言模型, 基准评估, 音频置换自一致性, 思维链, 输入缩放瓶颈

## 3 点简述
- 核心问题：多音频理解在大型音频-语言模型中未充分探索，性能随音频输入数量增加而急剧下降
- 方法要点：引入MUGEN基准，涵盖语音、通用音频和音乐，并研究训练免费策略如音频置换自一致性
- 实验或效果：音频置换自一致性提升准确率6.28%，结合思维链进一步改善至6.74%

## 摘要（原文）

> While multi-audio understanding is critical for large audio-language models (LALMs), it remains underexplored. We introduce MUGEN, a comprehensive benchmark evaluating this capability across speech, general audio, and music. Our experiments reveal consistent weaknesses in multi-audio settings, and performance degrades sharply as the number of concurrent audio inputs increases, identifying input scaling as a fundamental bottleneck. We further investigate training-free strategies and observe that Audio-Permutational Self-Consistency, which diversifies the order of audio candidates, helps models form more robust aggregated predictions, yielding up to 6.28% accuracy gains. Combining this permutation strategy with Chain-of-Thought further improves performance to 6.74%. These results expose blind spots in current LALMs and provide a foundation for evaluating complex auditory comprehension.

