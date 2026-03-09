---
layout: default
title: Imagine How To Change: Explicit Procedure Modeling for Change Captioning
---

# Imagine How To Change: Explicit Procedure Modeling for Change Captioning
**arXiv**：[2603.05969v1](https://arxiv.org/abs/2603.05969) · [PDF](https://arxiv.org/pdf/2603.05969.pdf)  
**作者**：Jiayang Sun, Zixin Guo, Min Cao, Guibo Zhu, Jorma Laaksonen  

**一句话要点**：提出ProCap框架，通过动态过程建模改进变化描述任务，从静态图像比较转向显式过程学习。

**关键词**：变化描述, 过程建模, 关键帧学习, 编码器-解码器, 端到端训练

## 3 点简述
- 核心问题：现有变化描述方法基于静态图像对，忽略变化过程的动态性，难以理解变化如何发生。
- 方法要点：采用两阶段设计，先训练过程编码器学习关键帧的潜在动态，再通过可学习查询集成到编码器-解码器模型中进行端到端训练。
- 实验或效果：在三个数据集上验证有效性，代码和预训练模型已开源。

## 摘要（原文）

> Change captioning generates descriptions that explicitly describe the differences between two visually similar images. Existing methods operate on static image pairs, thus ignoring the rich temporal dynamics of the change procedure, which is the key to understand not only what has changed but also how it occurs. We introduce ProCap, a novel framework that reformulates change modeling from static image comparison to dynamic procedure modeling. ProCap features a two-stage design: The first stage trains a procedure encoder to learn the change procedure from a sparse set of keyframes. These keyframes are obtained by automatically generating intermediate frames to make the implicit procedural dynamics explicit and then sampling them to mitigate redundancy. Then the encoder learns to capture the latent dynamics of these keyframes via a caption-conditioned, masked reconstruction task. The second stage integrates this trained encoder within an encoder-decoder model for captioning. Instead of relying on explicit frames from the previous stage -- a process incurring computational overhead and sensitivity to visual noise -- we introduce learnable procedure queries to prompt the encoder for inferring the latent procedure representation, which the decoder then translates into text. The entire model is then trained end-to-end with a captioning loss, ensuring the encoder's output is both temporally coherent and captioning-aligned. Experiments on three datasets demonstrate the effectiveness of ProCap. Code and pre-trained models are available at https://github.com/BlueberryOreo/ProCap

