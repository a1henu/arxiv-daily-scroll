---
layout: default
title: IBISAgent: Reinforcing Pixel-Level Visual Reasoning in MLLMs for Universal Biomedical Object Referring and Segmentation
---

# IBISAgent: Reinforcing Pixel-Level Visual Reasoning in MLLMs for Universal Biomedical Object Referring and Segmentation
**arXiv**：[2601.03054v1](https://arxiv.org/abs/2601.03054) · [PDF](https://arxiv.org/pdf/2601.03054.pdf)  
**作者**：Yankai Jiang, Qiaoru Li, Binlu Xu, Haoran Sun, Chao Ding, Junting Dong, Yuxiang Cai, Xuhong Zhang, Jianwei Yin  

**一句话要点**：提出IBISAgent以解决医学MLLMs像素级分割中的泛化与迭代优化问题

**关键词**：医学多模态大模型, 像素级视觉推理, 代理式分割, 迭代掩码优化, 强化学习训练

## 3 点简述
- 现有方法依赖隐式分割令牌和联合微调，易导致灾难性遗忘和泛化能力受限
- IBISAgent将分割重构为多步决策过程，通过推理和点击动作调用工具，无需架构修改
- 两阶段训练框架结合监督微调和强化学习，在复杂医学任务中实现SOTA性能

## 摘要（原文）

> Recent research on medical MLLMs has gradually shifted its focus from image-level understanding to fine-grained, pixel-level comprehension. Although segmentation serves as the foundation for pixel-level understanding, existing approaches face two major challenges. First, they introduce implicit segmentation tokens and require simultaneous fine-tuning of both the MLLM and external pixel decoders, which increases the risk of catastrophic forgetting and limits generalization to out-of-domain scenarios. Second, most methods rely on single-pass reasoning and lack the capability to iteratively refine segmentation results, leading to suboptimal performance. To overcome these limitations, we propose a novel agentic MLLM, named IBISAgent, that reformulates segmentation as a vision-centric, multi-step decision-making process. IBISAgent enables MLLMs to generate interleaved reasoning and text-based click actions, invoke segmentation tools, and produce high-quality masks without architectural modifications. By iteratively performing multi-step visual reasoning on masked image features, IBISAgent naturally supports mask refinement and promotes the development of pixel-level visual reasoning capabilities. We further design a two-stage training framework consisting of cold-start supervised fine-tuning and agentic reinforcement learning with tailored, fine-grained rewards, enhancing the model's robustness in complex medical referring and reasoning segmentation tasks. Extensive experiments demonstrate that IBISAgent consistently outperforms both closed-source and open-source SOTA methods. All datasets, code, and trained models will be released publicly.

