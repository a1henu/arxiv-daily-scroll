---
layout: default
title: ProtoQuant: Quantization of Prototypical Parts For General and Fine-Grained Image Classification
---

# ProtoQuant: Quantization of Prototypical Parts For General and Fine-Grained Image Classification
**arXiv**：[2602.06592v1](https://arxiv.org/abs/2602.06592) · [PDF](https://arxiv.org/pdf/2602.06592.pdf)  
**作者**：Mikołaj Janusz, Adam Wróbel, Bartosz Zieliński, Dawid Rymarczyk  

**一句话要点**：提出ProtoQuant，通过潜在向量量化实现原型稳定性和可解释性，用于通用和细粒度图像分类。

**关键词**：原型量化, 可解释性学习, 图像分类, 细粒度识别, 潜在向量量化

## 3 点简述
- 核心问题：原型漂移导致原型缺乏训练数据基础，影响可解释性和泛化能力。
- 方法要点：使用潜在向量量化约束原型到离散码本，无需更新骨干网络，提升效率和稳定性。
- 实验或效果：在ImageNet和细粒度基准测试中达到竞争性准确率，保持可解释性。

## 摘要（原文）

> Prototypical parts-based models offer a "this looks like that" paradigm for intrinsic interpretability, yet they typically struggle with ImageNet-scale generalization and often require computationally expensive backbone finetuning. Furthermore, existing methods frequently suffer from "prototype drift," where learned prototypes lack tangible grounding in the training distribution and change their activation under small perturbations. We present ProtoQuant, a novel architecture that achieves prototype stability and grounded interpretability through latent vector quantization. By constraining prototypes to a discrete learned codebook within the latent space, we ensure they remain faithful representations of the training data without the need to update the backbone. This design allows ProtoQuant to function as an efficient, interpretable head that scales to large-scale datasets. We evaluate ProtoQuant on ImageNet and several fine-grained benchmarks (CUB-200, Cars-196). Our results demonstrate that ProtoQuant achieves competitive classification accuracy while generalizing to ImageNet and comparable interpretability metrics to other prototypical-parts-based methods.

