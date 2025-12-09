---
layout: default
title: InterAgent: Physics-based Multi-agent Command Execution via Diffusion on Interaction Graphs
---

# InterAgent: Physics-based Multi-agent Command Execution via Diffusion on Interaction Graphs
**arXiv**：[2512.07410v1](https://arxiv.org/abs/2512.07410) · [PDF](https://arxiv.org/pdf/2512.07410.pdf)  
**作者**：Bin Li, Ruichi Zhang, Han Liang, Jingyan Zhang, Juze Zhang, Xin Chen, Lan Xu, Jingyi Yu, Jingya Wang  

**一句话要点**：提出InterAgent框架，通过交互图扩散实现基于物理的多智能体人形控制

**关键词**：多智能体控制, 物理模拟, 扩散模型, 交互图, 人形机器人, 文本驱动

## 3 点简述
- 核心问题：现有方法多局限于单智能体场景，缺乏物理合理的多智能体交互建模
- 方法要点：采用自回归扩散变换器与多流块，解耦本体感知、外感知和动作，并引入交互图外感知表示与稀疏边注意力机制
- 实验或效果：在实验中超越多个基线，实现从文本提示生成连贯、物理合理且语义忠实的行为

## 摘要（原文）

> Humanoid agents are expected to emulate the complex coordination inherent in human social behaviors. However, existing methods are largely confined to single-agent scenarios, overlooking the physically plausible interplay essential for multi-agent interactions. To bridge this gap, we propose InterAgent, the first end-to-end framework for text-driven physics-based multi-agent humanoid control. At its core, we introduce an autoregressive diffusion transformer equipped with multi-stream blocks, which decouples proprioception, exteroception, and action to mitigate cross-modal interference while enabling synergistic coordination. We further propose a novel interaction graph exteroception representation that explicitly captures fine-grained joint-to-joint spatial dependencies to facilitate network learning. Additionally, within it we devise a sparse edge-based attention mechanism that dynamically prunes redundant connections and emphasizes critical inter-agent spatial relations, thereby enhancing the robustness of interaction modeling. Extensive experiments demonstrate that InterAgent consistently outperforms multiple strong baselines, achieving state-of-the-art performance. It enables producing coherent, physically plausible, and semantically faithful multi-agent behaviors from only text prompts. Our code and data will be released to facilitate future research.

