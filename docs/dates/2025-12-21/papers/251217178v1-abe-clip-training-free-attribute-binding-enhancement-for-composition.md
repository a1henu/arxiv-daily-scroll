---
layout: default
title: ABE-CLIP: Training-Free Attribute Binding Enhancement for Compositional Image-Text Matching
---

# ABE-CLIP: Training-Free Attribute Binding Enhancement for Compositional Image-Text Matching
**arXiv**：[2512.17178v1](https://arxiv.org/abs/2512.17178) · [PDF](https://arxiv.org/pdf/2512.17178.pdf)  
**作者**：Qi Zhang, Yuxu Chen, Lei Deng, Lili Shen  

**一句话要点**：提出ABE-CLIP以无训练方式增强CLIP模型中的属性-对象绑定能力

**关键词**：组合图像-文本匹配, 属性-对象绑定, 无训练增强, 语义精炼, 局部对齐, CLIP模型

## 3 点简述
- CLIP在组合图像-文本匹配中因全局表示忽略细粒度语义而难以准确关联属性与对象
- ABE-CLIP通过语义精炼机制和局部令牌-补丁对齐策略，无需额外训练即可提升绑定性能
- 实验表明ABE-CLIP在多个数据集上显著改进绑定效果，甚至超越需训练的方法

## 摘要（原文）

> Contrastive Language-Image Pretraining (CLIP) has achieved remarkable performance in various multimodal tasks. However, it still struggles with compositional image-text matching, particularly in accurately associating objects with their corresponding attributes, because its inherent global representation often overlooks fine-grained semantics for attribute binding. Existing methods often require additional training or extensive hard negative sampling, yet they frequently show limited generalization to novel compositional concepts and fail to fundamentally address the drawbacks of global representations. In this paper, we propose ABE-CLIP, a novel training-free Attribute Binding Enhancement method designed to strengthen attribute-object binding in CLIP-like models. Specifically, we employ a Semantic Refinement Mechanism to refine token embeddings for both object and attribute phrases in the text, thereby mitigating attribute confusion and improving semantic precision. We further introduce a Local Token-Patch Alignment strategy that computes similarity scores between refined textual tokens and their most relevant image patches. By aggregating localized similarity scores, ABE-CLIP computes the final image-text similarity. Experiments on multiple datasets demonstrate that ABE-CLIP significantly improves attribute-object binding performance, even surpassing methods that require extensive training.

