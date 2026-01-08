---
layout: default
title: Klear: Unified Multi-Task Audio-Video Joint Generation
---

# Klear: Unified Multi-Task Audio-Video Joint Generation
**arXiv**：[2601.04151v1](https://arxiv.org/abs/2601.04151) · [PDF](https://arxiv.org/pdf/2601.04151.pdf)  
**作者**：Jun Wang, Chunyu Qiang, Yuxin Guo, Yiran Wang, Xijuan Zeng, Chen Zhang, Pengfei Wan  

**一句话要点**：提出Klear统一多任务音视频联合生成模型，解决音视频异步、唇语对齐差和模态退化问题。

**关键词**：音视频联合生成, 多任务学习, 统一架构, 数据增强, 模态对齐, 生成模型

## 3 点简述
- 核心问题：现有方法存在音视频异步、唇语对齐不佳和模态退化，源于弱对应建模、泛化有限和数据稀缺。
- 方法要点：采用单塔架构、统一DiT块和全注意力机制，结合渐进多任务训练和课程学习策略。
- 实验或效果：在大型数据集上实现高保真、语义时序对齐的生成，性能超越先前方法，与Veo 3相当。

## 摘要（原文）

> Audio-video joint generation has progressed rapidly, yet substantial challenges still remain. Non-commercial approaches still suffer audio-visual asynchrony, poor lip-speech alignment, and unimodal degradation, which can be stemmed from weak audio-visual correspondence modeling, limited generalization, and scarce high-quality dense-caption data. To address these issues, we introduce Klear and delve into three axes--model architecture, training strategy, and data curation. Architecturally, we adopt a single-tower design with unified DiT blocks and an Omni-Full Attention mechanism, achieving tight audio-visual alignment and strong scalability. Training-wise, we adopt a progressive multitask regime--random modality masking to joint optimization across tasks, and a multistage curriculum, yielding robust representations, strengthening A-V aligned world knowledge, and preventing unimodal collapse. For datasets, we present the first large-scale audio-video dataset with dense captions, and introduce a novel automated data-construction pipeline which annotates and filters millions of diverse, high-quality, strictly aligned audio-video-caption triplets. Building on this, Klear scales to large datasets, delivering high-fidelity, semantically and temporally aligned, instruction-following generation in both joint and unimodal settings while generalizing robustly to out-of-distribution scenarios. Across tasks, it substantially outperforms prior methods by a large margin and achieves performance comparable to Veo 3, offering a unified, scalable path toward next-generation audio-video synthesis.

