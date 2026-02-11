---
layout: default
title: CAPER: Constrained and Procedural Reasoning for Robotic Scientific Experiments
---

# CAPER: Constrained and Procedural Reasoning for Robotic Scientific Experiments
**arXiv**：[2602.09367v1](https://arxiv.org/abs/2602.09367) · [PDF](https://arxiv.org/pdf/2602.09367.pdf)  
**作者**：Jinghan Yang, Jingyi Hou, Xinbo Yu, Wei He, Yifan Wu  

**一句话要点**：提出CAPER框架以解决机器人科学实验中长时程操作和低演示数据下的鲁棒性问题

**关键词**：机器人科学实验, 长时程操作, 程序推理, 多模态接地, 强化学习, 低演示数据

## 3 点简述
- 核心问题：端到端视觉-语言-动作模型在协议敏感实验中易失效，需处理长时程操作和低监督下的鲁棒性。
- 方法要点：采用责任分离结构，通过任务级推理、中层多模态接地和低层控制，编码可解释中间表示。
- 实验或效果：在科学工作流基准和长时程操作数据集上，提升成功率和程序正确性，尤其在低数据和长时程场景。

## 摘要（原文）

> Robotic assistance in scientific laboratories requires procedurally correct long-horizon manipulation, reliable execution under limited supervision, and robustness in low-demonstration regimes. Such conditions greatly challenge end-to-end vision-language-action (VLA) models, whose assumptions of recoverable errors and data-driven policy learning often break down in protocol-sensitive experiments. We propose CAPER, a framework for Constrained And ProcEdural Reasoning for robotic scientific experiments, which explicitly restricts where learning and reasoning occur in the planning and control pipeline. Rather than strengthening end-to-end policies, CAPER enforces a responsibility-separated structure: task-level reasoning generates procedurally valid action sequences under explicit constraints, mid-level multimodal grounding realizes subtasks without delegating spatial decision-making to large language models, and low-level control adapts to physical uncertainty via reinforcement learning with minimal demonstrations. By encoding procedural commitments through interpretable intermediate representations, CAPER prevents execution-time violations of experimental logic, improving controllability, robustness, and data efficiency. Experiments on a scientific workflow benchmark and a public long-horizon manipulation dataset demonstrate consistent improvements in success rate and procedural correctness, particularly in low-data and long-horizon settings.

