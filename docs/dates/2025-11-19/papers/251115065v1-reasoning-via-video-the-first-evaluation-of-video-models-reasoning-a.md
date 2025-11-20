---
layout: default
title: Reasoning via Video: The First Evaluation of Video Models' Reasoning Abilities through Maze-Solving Tasks
---

# Reasoning via Video: The First Evaluation of Video Models' Reasoning Abilities through Maze-Solving Tasks
**arXiv**：[2511.15065v1](https://arxiv.org/abs/2511.15065) · [PDF](https://arxiv.org/pdf/2511.15065.pdf)  
**作者**：Cheng Yang, Haiyuan Wan, Yiran Peng, Xin Cheng, Zhaoyang Yu, Jiayi Zhang, Junchi Yu, Xinlei Yu, Xiawu Zheng, Dongzhan Zhou, Chenglin Wu  

**一句话要点**：提出VR-Bench基准以评估视频模型在迷宫求解任务中的推理能力

**关键词**：视频推理, 空间推理, 迷宫求解, 视频生成, 基准评估, 监督微调

## 3 点简述
- 核心问题：视频模型能否通过视频生成进行空间推理，类比文本模型从生成到推理的发展
- 方法要点：基于迷宫求解任务构建VR-Bench，包含7920个程序生成视频，支持空间规划与多步推理评估
- 实验或效果：SFT有效激发推理能力，视频模型在空间感知上优于VLMs，推理可靠性提升10-20%

## 摘要（原文）

> Video Models have achieved remarkable success in high-fidelity video generation with coherent motion dynamics. Analogous to the development from text generation to text-based reasoning in language modeling, the development of video models motivates us to ask: Can video models reason via video generation? Compared with the discrete text corpus, video grounds reasoning in explicit spatial layouts and temporal continuity, which serves as an ideal substrate for spatial reasoning. In this work, we explore the reasoning via video paradigm and introduce VR-Bench -- a comprehensive benchmark designed to systematically evaluate video models' reasoning capabilities. Grounded in maze-solving tasks that inherently require spatial planning and multi-step reasoning, VR-Bench contains 7,920 procedurally generated videos across five maze types and diverse visual styles. Our empirical analysis demonstrates that SFT can efficiently elicit the reasoning ability of video model. Video models exhibit stronger spatial perception during reasoning, outperforming leading VLMs and generalizing well across diverse scenarios, tasks, and levels of complexity. We further discover a test-time scaling effect, where diverse sampling during inference improves reasoning reliability by 10--20%. These findings highlight the unique potential and scalability of reasoning via video for spatial reasoning tasks.

