---
layout: default
title: Visual Bridge: Universal Visual Perception Representations Generating
---

# Visual Bridge: Universal Visual Perception Representations Generating
**arXiv**：[2511.07877v1](https://arxiv.org/abs/2511.07877) · [PDF](https://arxiv.org/pdf/2511.07877.pdf)  
**作者**：Yilin Gao, Shuguang Dou, Junzhou Li, Zhiheng Yu, Yin Li, Dongsheng Jiang, Shugong Xu  

**一句话要点**：提出基于流匹配的通用视觉感知框架，以解决多任务场景下的泛化与扩展性问题。

**关键词**：通用视觉感知, 流匹配, 多任务学习, 视觉表示生成, 零样本学习

## 3 点简述
- 核心问题：现有扩散模型局限于单任务单模型范式，泛化与扩展性不足。
- 方法要点：使用流匹配从图像块令牌生成任务特定表示，引入多尺度循环任务嵌入。
- 实验或效果：在分类、检测等任务中，零样本和微调设置下性能优于先前模型。

## 摘要（原文）

> Recent advances in diffusion models have achieved remarkable success in isolated computer vision tasks such as text-to-image generation, depth estimation, and optical flow. However, these models are often restricted by a ``single-task-single-model'' paradigm, severely limiting their generalizability and scalability in multi-task scenarios. Motivated by the cross-domain generalization ability of large language models, we propose a universal visual perception framework based on flow matching that can generate diverse visual representations across multiple tasks. Our approach formulates the process as a universal flow-matching problem from image patch tokens to task-specific representations rather than an independent generation or regression problem. By leveraging a strong self-supervised foundation model as the anchor and introducing a multi-scale, circular task embedding mechanism, our method learns a universal velocity field to bridge the gap between heterogeneous tasks, supporting efficient and flexible representation transfer. Extensive experiments on classification, detection, segmentation, depth estimation, and image-text retrieval demonstrate that our model achieves competitive performance in both zero-shot and fine-tuned settings, outperforming prior generalist and several specialist models. Ablation studies further validate the robustness, scalability, and generalization of our framework. Our work marks a significant step towards general-purpose visual perception, providing a solid foundation for future research in universal vision modeling.

