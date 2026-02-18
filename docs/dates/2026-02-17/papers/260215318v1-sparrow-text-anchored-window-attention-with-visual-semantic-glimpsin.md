---
layout: default
title: Sparrow: Text-Anchored Window Attention with Visual-Semantic Glimpsing for Speculative Decoding in Video LLMs
---

# Sparrow: Text-Anchored Window Attention with Visual-Semantic Glimpsing for Speculative Decoding in Video LLMs
**arXiv**：[2602.15318v1](https://arxiv.org/abs/2602.15318) · [PDF](https://arxiv.org/pdf/2602.15318.pdf)  
**作者**：Libo Zhang, Zhaoning Zhang, Wangyang Hong, Peng Qiao, Dongsheng Li  

**一句话要点**：提出Sparrow框架以解决视频大语言模型中推测解码的性能崩溃问题

**关键词**：视频大语言模型, 推测解码, 注意力机制, 视觉语义内部化, 多令牌预测, 长视频任务

## 3 点简述
- 核心问题：推测解码在视频大语言模型中因注意力稀释和负视觉增益导致性能崩溃
- 方法要点：利用文本锚定窗口注意力和中间层视觉状态桥接，卸载视觉计算并过滤低层噪声
- 实验或效果：在25k视觉令牌下平均加速2.82倍，有效缓解长序列性能下降

## 摘要（原文）

> Although speculative decoding is widely used to accelerate Vision-Language Models (VLMs) inference, it faces severe performance collapse when applied to Video Large Language Models (Vid-LLMs). The draft model typically falls into the trap of attention dilution and negative visual gain due to key-value cache explosion and context window mismatches. We observe a visual semantic internalization phenomenon in Vid-LLMs, indicating that critical visual semantics are implicitly encoded into text hidden states during deep-layer interactions, which renders raw visual inputs structurally redundant during deep inference. To address this, we propose the Sparrow framework, which first utilizes visually-aware text-anchored window attention via hidden state reuse to fully offload visual computation to the target model, and leverages intermediate-layer visual state bridging to train the draft model with semantic-rich intermediate states, thereby filtering out low-level visual noise. Additionally, a multi-token prediction strategy is introduced to bridge the training-inference distribution shift. Experiments show that Sparrow achieves an average speedup of 2.82x even with 25k visual tokens, effectively resolving the performance degradation in long sequences and offering a practical solution for real-time long video tasks.

