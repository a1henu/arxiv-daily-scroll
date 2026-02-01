---
layout: default
title: Identifiable Equivariant Networks are Layerwise Equivariant
---

# Identifiable Equivariant Networks are Layerwise Equivariant
**arXiv**：[2601.21645v1](https://arxiv.org/abs/2601.21645) · [PDF](https://arxiv.org/pdf/2601.21645.pdf)  
**作者**：Vahid Shahverdi, Giovanni Luca Marchetti, Georg Bökman, Kathlén Kohn  

**一句话要点**：证明可识别等变网络的层间等变性，解释训练中等变结构的涌现

**关键词**：等变性网络, 参数可识别性, 层间等变性, 深度神经网络理论, 群作用

## 3 点简述
- 研究深度神经网络端到端等变性与层间等变性的关系
- 基于参数可识别性假设，证明存在参数选择使层具有等变性
- 理论架构无关，为实践中权重等变结构的出现提供数学解释

## 摘要（原文）

> We investigate the relation between end-to-end equivariance and layerwise equivariance in deep neural networks. We prove the following: For a network whose end-to-end function is equivariant with respect to group actions on the input and output spaces, there is a parameter choice yielding the same end-to-end function such that its layers are equivariant with respect to some group actions on the latent spaces. Our result assumes that the parameters of the model are identifiable in an appropriate sense. This identifiability property has been established in the literature for a large class of networks, to which our results apply immediately, while it is conjectural for others. The theory we develop is grounded in an abstract formalism, and is therefore architecture-agnostic. Overall, our results provide a mathematical explanation for the emergence of equivariant structures in the weights of neural networks during training -- a phenomenon that is consistently observed in practice.

