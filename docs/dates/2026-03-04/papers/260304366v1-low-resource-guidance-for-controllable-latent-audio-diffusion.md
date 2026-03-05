---
layout: default
title: Low-Resource Guidance for Controllable Latent Audio Diffusion
---

# Low-Resource Guidance for Controllable Latent Audio Diffusion
**arXiv**：[2603.04366v1](https://arxiv.org/abs/2603.04366) · [PDF](https://arxiv.org/pdf/2603.04366.pdf)  
**作者**：Zachary Novack, Zack Zukowski, CJ Carr, Julian Parker, Zach Evans, Josiah Taylor, Taylor Berg-Kirkpatrick, Julian McAuley, Jordi Pons  

**一句话要点**：提出LatCHs方法以低资源实现潜在音频扩散模型的可控生成

**关键词**：潜在音频扩散, 可控生成, 低资源引导, 计算效率, 音频质量, 选择性TFG

## 3 点简述
- 核心问题：现有可控音频生成方法需模型重训练或推理时高计算成本的引导
- 方法要点：通过选择性TFG和LatCHs在潜在空间操作，避免解码器反向传播，降低计算开销
- 实验或效果：在Stable Audio Open上有效控制强度、音高和节拍，保持生成质量，训练仅需7M参数和约4小时

## 摘要（原文）

> Generative audio requires fine-grained controllable outputs, yet most existing methods require model retraining on specific controls or inference-time controls (\textit{e.g.}, guidance) that can also be computationally demanding. By examining the bottlenecks of existing guidance-based controls, in particular their high cost-per-step due to decoder backpropagation, we introduce a guidance-based approach through selective TFG and Latent-Control Heads (LatCHs), which enables controlling latent audio diffusion models with low computational overhead. LatCHs operate directly in latent space, avoiding the expensive decoder step, and requiring minimal training resources (7M parameters and $\approx$ 4 hours of training). Experiments with Stable Audio Open demonstrate effective control over intensity, pitch, and beats (and a combination of those) while maintaining generation quality. Our method balances precision and audio fidelity with far lower computational costs than standard end-to-end guidance. Demo examples can be found at https://zacharynovack.github.io/latch/latch.html.

