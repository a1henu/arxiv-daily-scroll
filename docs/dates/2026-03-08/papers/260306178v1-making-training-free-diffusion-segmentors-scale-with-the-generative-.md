---
layout: default
title: Making Training-Free Diffusion Segmentors Scale with the Generative Power
---

# Making Training-Free Diffusion Segmentors Scale with the Generative Power
**arXiv**：[2603.06178v1](https://arxiv.org/abs/2603.06178) · [PDF](https://arxiv.org/pdf/2603.06178.pdf)  
**作者**：Benyuan Meng, Qianqian Xu, Zitai Wang, Xiaochun Cao, Longtao Huang, Qingming Huang  

**一句话要点**：提出自动聚合与逐像素重缩放技术，以提升无训练扩散分割器的生成能力利用效果。

**关键词**：无训练分割, 扩散模型, 跨注意力, 语义分割, 生成能力利用

## 3 点简述
- 现有无训练扩散分割方法未能随生成模型能力提升而有效扩展，存在跨注意力图不一致与得分不平衡问题。
- 通过自动聚合统一多层多头注意力图，并采用逐像素重缩放平衡文本令牌得分，增强语义相关性。
- 在标准语义分割基准上验证性能提升，并集成到生成技术中展示广泛适用性。

## 摘要（原文）

> As powerful generative models, text-to-image diffusion models have recently been explored for discriminative tasks. A line of research focuses on adapting a pre-trained diffusion model to semantic segmentation without any further training, leading to what training-free diffusion segmentors. These methods typically rely on cross-attention maps from the model's attention layers, which are assumed to capture semantic relationships between image pixels and text tokens. Ideally, such approaches should benefit from more powerful diffusion models, i.e., stronger generative capability should lead to better segmentation. However, we observe that existing methods often fail to scale accordingly. To understand this issue, we identify two underlying gaps: (i) cross-attention is computed across multiple heads and layers, but there exists a discrepancy between these individual attention maps and a unified global representation. (ii) Even when a global map is available, it does not directly translate to accurate semantic correlation for segmentation, due to score imbalances among different text tokens. To bridge these gaps, we propose two techniques: auto aggregation and per-pixel rescaling, which together enable training-free segmentation to better leverage generative capability. We evaluate our approach on standard semantic segmentation benchmarks and further integrate it into a generative technique, demonstrating both improved performance broad applicability. Codes are at https://github.com/Darkbblue/goca.

