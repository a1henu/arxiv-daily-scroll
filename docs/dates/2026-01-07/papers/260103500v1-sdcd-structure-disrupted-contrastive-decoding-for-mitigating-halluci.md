---
layout: default
title: SDCD: Structure-Disrupted Contrastive Decoding for Mitigating Hallucinations in Large Vision-Language Models
---

# SDCD: Structure-Disrupted Contrastive Decoding for Mitigating Hallucinations in Large Vision-Language Models
**arXiv**：[2601.03500v1](https://arxiv.org/abs/2601.03500) · [PDF](https://arxiv.org/pdf/2601.03500.pdf)  
**作者**：Yuxuan Xia, Siheng Wang, Peng Li  

**一句话要点**：提出SDCD算法以缓解大视觉语言模型中的物体幻觉问题

**关键词**：大视觉语言模型, 物体幻觉, 视觉统计偏差, 对比解码, 结构打乱, 训练无关算法

## 3 点简述
- 核心问题：视觉编码器在弱结构监督下产生视觉统计偏差，导致模型过度依赖局部纹理特征而忽视整体几何结构，引发物体幻觉。
- 方法要点：引入训练无关的SDCD算法，通过结构打乱的对比解码，惩罚在结构缺失视图中保持高置信度的令牌，抑制纹理驱动偏差。
- 实验或效果：SDCD在多个基准测试中显著缓解幻觉，并提升大视觉语言模型的多模态能力。

## 摘要（原文）

> Large Vision-Language Models (LVLMs) demonstrate significant progress in multimodal understanding and reasoning, yet object hallucination remains a critical challenge. While existing research focuses on mitigating language priors or high-level statistical biases, they often overlook the internal complexities of the visual encoding process. We identify that visual statistical bias, arising from the inherent Bag-of-Patches behavior of Vision Encoders under weak structural supervision, acts as a contributing factor of object hallucinations. Under this bias, models prioritize local texture features within individual patches over holistic geometric structures. This tendency may induce spurious visual confidence and result in hallucinations. To address this, we introduce a training-free algorithm called Structure-Disrupted Contrastive Decoding (SDCD), which performs contrastive calibration of the output distribution by introducing a shuffled structure-disrupted view. By penalizing tokens that maintain high confidence under this structure-less view, SDCD effectively suppresses the texture-driven bias. Experimental results demonstrate that SDCD significantly mitigates hallucinations across multiple benchmarks and enhances the overall multimodal capabilities of LVLMs.

