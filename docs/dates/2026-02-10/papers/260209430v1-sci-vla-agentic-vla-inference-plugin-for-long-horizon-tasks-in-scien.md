---
layout: default
title: Sci-VLA: Agentic VLA Inference Plugin for Long-Horizon Tasks in Scientific Experiments
---

# Sci-VLA: Agentic VLA Inference Plugin for Long-Horizon Tasks in Scientific Experiments
**arXiv**：[2602.09430v1](https://arxiv.org/abs/2602.09430) · [PDF](https://arxiv.org/pdf/2602.09430.pdf)  
**作者**：Yiwen Pang, Bo Zhou, Changjin Li, Xuanhao Wang, Shengxiang Xu, Deng-Bao Wang, Min-Ling Zhang, Shimin Di  

**一句话要点**：提出Sci-VLA插件，通过LLM代理推理解决科学实验中长时程任务的过渡操作缺失问题。

**关键词**：视觉语言动作模型, 长时程任务, 科学实验自动化, 代理推理, 过渡操作生成, 仿真到现实迁移

## 3 点简述
- 核心问题：VLA模型在科学实验中执行复合任务时，因训练与推理分布不匹配而无法处理原子任务间的过渡操作。
- 方法要点：引入基于LLM的代理推理机制，在推理时生成过渡性机器人动作代码，无需额外训练。
- 实验或效果：在仿真环境中验证，平均原子任务成功率提升42%，并可迁移至真实实验室。

## 摘要（原文）

> Robotic laboratories play a critical role in autonomous scientific discovery by enabling scalable, continuous experimental execution. Recent vision-language-action (VLA) models offer a promising foundation for robotic laboratories. However, scientific experiments typically involve long-horizon tasks composed of multiple atomic tasks, posing a fundamental challenge to existing VLA models. While VLA models fine-tuned for scientific tasks can reliably execute atomic experimental actions seen during training, they often fail to perform composite tasks formed by reordering and composing these known atomic actions. This limitation arises from a distributional mismatch between training-time atomic tasks and inference-time composite tasks, which prevents VLA models from executing necessary transitional operations between atomic tasks. To address this challenge, we propose an Agentic VLA Inference Plugin for Long-Horizon Tasks in Scientific Experiments. It introduces an LLM-based agentic inference mechanism that intervenes when executing sequential manipulation tasks. By performing explicit transition inference and generating transitional robotic action code, the proposed plugin guides VLA models through missing transitional steps, enabling reliable execution of composite scientific workflows without any additional training. This inference-only intervention makes our method computationally efficient, data-efficient, and well-suited for open-ended and long-horizon robotic laboratory tasks. We build 3D assets of scientific instruments and common scientific operating scenes within an existing simulation environment. In these scenes, we have verified that our method increases the average success rate per atomic task by 42\% during inference. Furthermore, we show that our method can be easily transferred from the simulation to real scientific laboratories.

