---
layout: default
title: DashFusion: Dual-stream Alignment with Hierarchical Bottleneck Fusion for Multimodal Sentiment Analysis
---

# DashFusion: Dual-stream Alignment with Hierarchical Bottleneck Fusion for Multimodal Sentiment Analysis
**arXiv**：[2512.05515v1](https://arxiv.org/abs/2512.05515) · [PDF](https://arxiv.org/pdf/2512.05515.pdf)  
**作者**：Yuhua Wen, Qifei Li, Yingying Zhou, Yingming Gao, Zhengqi Wen, Jianhua Tao, Ya Li  

**一句话要点**：提出DashFusion框架，通过双流对齐与分层瓶颈融合解决多模态情感分析中的对齐与融合问题。

**关键词**：多模态情感分析, 跨模态对齐, 分层融合, 监督对比学习, 计算效率优化

## 3 点简述
- 核心问题：多模态情感分析面临跨模态时序与语义对齐及特征融合的挑战，现有方法常孤立处理导致性能受限。
- 方法要点：采用双流对齐模块实现时序与语义同步，结合监督对比学习优化特征，并通过分层瓶颈融合平衡性能与效率。
- 实验或效果：在CMU-MOSI等数据集上达到先进性能，消融研究验证了对齐与融合技术的有效性。

## 摘要（原文）

> Multimodal sentiment analysis (MSA) integrates various modalities, such as text, image, and audio, to provide a more comprehensive understanding of sentiment. However, effective MSA is challenged by alignment and fusion issues. Alignment requires synchronizing both temporal and semantic information across modalities, while fusion involves integrating these aligned features into a unified representation. Existing methods often address alignment or fusion in isolation, leading to limitations in performance and efficiency. To tackle these issues, we propose a novel framework called Dual-stream Alignment with Hierarchical Bottleneck Fusion (DashFusion). Firstly, dual-stream alignment module synchronizes multimodal features through temporal and semantic alignment. Temporal alignment employs cross-modal attention to establish frame-level correspondences among multimodal sequences. Semantic alignment ensures consistency across the feature space through contrastive learning. Secondly, supervised contrastive learning leverages label information to refine the modality features. Finally, hierarchical bottleneck fusion progressively integrates multimodal information through compressed bottleneck tokens, which achieves a balance between performance and computational efficiency. We evaluate DashFusion on three datasets: CMU-MOSI, CMU-MOSEI, and CH-SIMS. Experimental results demonstrate that DashFusion achieves state-of-the-art performance across various metrics, and ablation studies confirm the effectiveness of our alignment and fusion techniques. The codes for our experiments are available at https://github.com/ultramarineX/DashFusion.

