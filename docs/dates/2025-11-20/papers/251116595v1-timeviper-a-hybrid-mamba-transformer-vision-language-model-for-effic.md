---
layout: default
title: TimeViper: A Hybrid Mamba-Transformer Vision-Language Model for Efficient Long Video Understanding
---

# TimeViper: A Hybrid Mamba-Transformer Vision-Language Model for Efficient Long Video Understanding
**arXiv**：[2511.16595v1](https://arxiv.org/abs/2511.16595) · [PDF](https://arxiv.org/pdf/2511.16595.pdf)  
**作者**：Boshen Xu, Zihan Xiao, Jiaze Li, Jianzhong Ju, Zhenbo Luo, Jian Luan, Qin Jin  

**一句话要点**：提出TimeViper混合模型以高效处理长视频理解问题

**关键词**：长视频理解, 混合模型, 令牌压缩, 状态空间模型, 视觉语言模型, 模型解释性

## 3 点简述
- 核心问题：长视频处理需高效架构和扩展时间上下文机制
- 方法要点：结合Mamba状态空间模型与Transformer注意力，设计TransV模块压缩视觉令牌
- 实验或效果：在多个基准测试中与先进模型竞争，可处理超万帧小时级视频

## 摘要（原文）

> We introduce TimeViper, a hybrid vision-language model designed to tackle challenges of long video understanding. Processing long videos demands both an efficient model architecture and an effective mechanism for handling extended temporal contexts. To this end, TimeViper adopts a hybrid Mamba-Transformer backbone that combines the efficiency of state-space models with the expressivity of attention mechanisms. Through this hybrid design, we reveal the vision-to-text information aggregation phenomenon, where information progressively flows from vision tokens to text tokens across increasing LLM depth, resulting in severe vision token redundancy. Motivated by this observation, we propose TransV, a token information transfer module that transfers and compresses vision tokens into instruction tokens while maintaining multimodal understanding capabilities. This design enables TimeViper to process hour-long videos exceeding 10,000 frames. Extensive experiments across multiple benchmarks demonstrate that TimeViper competes with state-of-the-art models while extending frame numbers. We further analyze attention behaviors of both Mamba and Transformer layers, offering new insights into hybrid model interpretability. This work represents an initial step towards developing, interpreting, and compressing hybrid Mamba-Transformer architectures.

