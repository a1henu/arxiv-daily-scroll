---
layout: default
title: Improved Mean Flows: On the Challenges of Fastforward Generative Models
---

# Improved Mean Flows: On the Challenges of Fastforward Generative Models
**arXiv**：[2512.02012v1](https://arxiv.org/abs/2512.02012) · [PDF](https://arxiv.org/pdf/2512.02012.pdf)  
**作者**：Zhengyang Geng, Yiyang Lu, Zongze Wu, Eli Shechtman, J. Zico Kolter, Kaiming He  

**一句话要点**：提出改进MeanFlow以解决单步生成模型中的训练不稳定和引导灵活性不足问题。

**关键词**：单步生成模型, 训练稳定性, 引导机制, 上下文条件, 图像生成, 平均速度预测

## 3 点简述
- 原MeanFlow训练目标依赖网络自身，导致不稳定；本文重参数化为平均速度预测，提升回归稳定性。
- 原方法固定训练时引导尺度，牺牲灵活性；本文通过显式条件变量实现测试时灵活引导，并采用上下文条件处理。
- 改进方法在ImageNet 256×256上实现1.72 FID（1-NFE），优于同类方法，缩小与多步方法的差距。

## 摘要（原文）

> MeanFlow (MF) has recently been established as a framework for one-step generative modeling. However, its ``fastforward'' nature introduces key challenges in both the training objective and the guidance mechanism. First, the original MF's training target depends not only on the underlying ground-truth fields but also on the network itself. To address this issue, we recast the objective as a loss on the instantaneous velocity $v$, re-parameterized by a network that predicts the average velocity $u$. Our reformulation yields a more standard regression problem and improves the training stability. Second, the original MF fixes the classifier-free guidance scale during training, which sacrifices flexibility. We tackle this issue by formulating guidance as explicit conditioning variables, thereby retaining flexibility at test time. The diverse conditions are processed through in-context conditioning, which reduces model size and benefits performance. Overall, our $\textbf{improved MeanFlow}$ ($\textbf{iMF}$) method, trained entirely from scratch, achieves $\textbf{1.72}$ FID with a single function evaluation (1-NFE) on ImageNet 256$\times$256. iMF substantially outperforms prior methods of this kind and closes the gap with multi-step methods while using no distillation. We hope our work will further advance fastforward generative modeling as a stand-alone paradigm.

