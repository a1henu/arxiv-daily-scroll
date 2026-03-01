---
layout: default
title: WISER: Wider Search, Deeper Thinking, and Adaptive Fusion for Training-Free Zero-Shot Composed Image Retrieval
---

# WISER: Wider Search, Deeper Thinking, and Adaptive Fusion for Training-Free Zero-Shot Composed Image Retrieval
**arXiv**：[2602.23029v1](https://arxiv.org/abs/2602.23029) · [PDF](https://arxiv.org/pdf/2602.23029.pdf)  
**作者**：Tianyue Wang, Leigang Qu, Tianyu Yang, Xiangzhao Hao, Yifan Xu, Haiyun Guo, Jinqiao Wang  

**一句话要点**：提出WISER框架，通过检索-验证-精炼流程统一T2I和I2I，以解决零样本组合图像检索中模态转换的局限性。

**关键词**：零样本组合图像检索, 训练免费框架, 多模态融合, 意图感知, 不确定性建模, 检索验证精炼

## 3 点简述
- 零样本组合图像检索中，现有方法将多模态查询转为单一模态，导致T2I丢失视觉细节或I2I难以处理复杂语义修改。
- WISER采用训练免费方法，通过并行检索生成编辑标题和图像，并基于验证器动态融合双路径，以增强意图和不确定性感知。
- 实验显示，WISER在CIRCO和CIRR基准上显著优于先前方法，相对提升达45%和57%，甚至超越部分训练依赖方法。

## 摘要（原文）

> Zero-Shot Composed Image Retrieval (ZS-CIR) aims to retrieve target images given a multimodal query (comprising a reference image and a modification text), without training on annotated triplets. Existing methods typically convert the multimodal query into a single modality-either as an edited caption for Text-to-Image retrieval (T2I) or as an edited image for Image-to-Image retrieval (I2I). However, each paradigm has inherent limitations: T2I often loses fine-grained visual details, while I2I struggles with complex semantic modifications. To effectively leverage their complementary strengths under diverse query intents, we propose WISER, a training-free framework that unifies T2I and I2I via a "retrieve-verify-refine" pipeline, explicitly modeling intent awareness and uncertainty awareness. Specifically, WISER first performs Wider Search by generating both edited captions and images for parallel retrieval to broaden the candidate pool. Then, it conducts Adaptive Fusion with a verifier to assess retrieval confidence, triggering refinement for uncertain retrievals, and dynamically fusing the dual-path for reliable ones. For uncertain retrievals, WISER generates refinement suggestions through structured self-reflection to guide the next retrieval round toward Deeper Thinking. Extensive experiments demonstrate that WISER significantly outperforms previous methods across multiple benchmarks, achieving relative improvements of 45% on CIRCO (mAP@5) and 57% on CIRR (Recall@1) over existing training-free methods. Notably, it even surpasses many training-dependent methods, highlighting its superiority and generalization under diverse scenarios. Code will be released at https://github.com/Physicsmile/WISER.

