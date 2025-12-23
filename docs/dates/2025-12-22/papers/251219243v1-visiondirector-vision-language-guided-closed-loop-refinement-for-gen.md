---
layout: default
title: VisionDirector: Vision-Language Guided Closed-Loop Refinement for Generative Image Synthesis
---

# VisionDirector: Vision-Language Guided Closed-Loop Refinement for Generative Image Synthesis
**arXiv**：[2512.19243v1](https://arxiv.org/abs/2512.19243) · [PDF](https://arxiv.org/pdf/2512.19243.pdf)  
**作者**：Meng Chu, Senqiao Yang, Haoxuan Che, Suiyun Zhang, Xichen Zhang, Shaozuo Yu, Haokun Gui, Zhefan Rao, Dandan Tu, Rui Liu, Jiaya Jia  

**一句话要点**：提出VisionDirector以解决生成模型处理长多目标提示时的对齐问题

**关键词**：生成图像合成, 视觉语言模型, 长目标提示, 闭环细化, 对齐评估, 微网格采样

## 3 点简述
- 核心问题：生成模型难以满足专业设计师的长多目标提示，现有方法对齐率低。
- 方法要点：VisionDirector通过训练免费的视觉语言监督器，实现结构化目标提取、动态编辑决策和微网格采样验证。
- 实验或效果：在LGBench等基准上实现新SOTA，提升对齐率并缩短编辑步骤。

## 摘要（原文）

> Generative models can now produce photorealistic imagery, yet they still struggle with the long, multi-goal prompts that professional designers issue. To expose this gap and better evaluate models' performance in real-world settings, we introduce Long Goal Bench (LGBench), a 2,000-task suite (1,000 T2I and 1,000 I2I) whose average instruction contains 18 to 22 tightly coupled goals spanning global layout, local object placement, typography, and logo fidelity. We find that even state-of-the-art models satisfy fewer than 72 percent of the goals and routinely miss localized edits, confirming the brittleness of current pipelines. To address this, we present VisionDirector, a training-free vision-language supervisor that (i) extracts structured goals from long instructions, (ii) dynamically decides between one-shot generation and staged edits, (iii) runs micro-grid sampling with semantic verification and rollback after every edit, and (iv) logs goal-level rewards. We further fine-tune the planner with Group Relative Policy Optimization, yielding shorter edit trajectories (3.1 versus 4.2 steps) and stronger alignment. VisionDirector achieves new state of the art on GenEval (plus 7 percent overall) and ImgEdit (plus 0.07 absolute) while producing consistent qualitative improvements on typography, multi-object scenes, and pose editing.

