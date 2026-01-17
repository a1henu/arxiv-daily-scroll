---
layout: default
title: CoF-T2I: Video Models as Pure Visual Reasoners for Text-to-Image Generation
---

# CoF-T2I: Video Models as Pure Visual Reasoners for Text-to-Image Generation
**arXiv**：[2601.10061v1](https://arxiv.org/abs/2601.10061) · [PDF](https://arxiv.org/pdf/2601.10061.pdf)  
**作者**：Chengzhuo Tong, Mingkun Chang, Shenglong Zhang, Yuran Wang, Cheng Liang, Zhizheng Zhao, Ruichuan An, Bohan Zeng, Yang Shi, Yifan Dai, Ziming Zhao, Guanbin Li, Pengfei Wan, Yuanxing Zhang, Wentao Zhang  

**一句话要点**：提出CoF-T2I，通过链式帧推理增强文本到图像生成，实现渐进视觉细化。

**关键词**：链式帧推理, 文本到图像生成, 渐进视觉细化, 视频模型应用, 数据集构建

## 3 点简述
- 问题：文本到图像生成缺乏明确视觉推理起点和可解释中间状态，限制视频模型应用。
- 方法：集成链式帧推理，以中间帧为显式推理步骤，最终帧输出，并构建CoF-Evol-Instruct数据集建模生成过程。
- 效果：在GenEval和Imagine-Bench上表现优异，超越基础视频模型，展示视频模型提升图像生成质量的潜力。

## 摘要（原文）

> Recent video generation models have revealed the emergence of Chain-of-Frame (CoF) reasoning, enabling frame-by-frame visual inference. With this capability, video models have been successfully applied to various visual tasks (e.g., maze solving, visual puzzles). However, their potential to enhance text-to-image (T2I) generation remains largely unexplored due to the absence of a clearly defined visual reasoning starting point and interpretable intermediate states in the T2I generation process. To bridge this gap, we propose CoF-T2I, a model that integrates CoF reasoning into T2I generation via progressive visual refinement, where intermediate frames act as explicit reasoning steps and the final frame is taken as output. To establish such an explicit generation process, we curate CoF-Evol-Instruct, a dataset of CoF trajectories that model the generation process from semantics to aesthetics. To further improve quality and avoid motion artifacts, we enable independent encoding operation for each frame. Experiments show that CoF-T2I significantly outperforms the base video model and achieves competitive performance on challenging benchmarks, reaching 0.86 on GenEval and 7.468 on Imagine-Bench. These results indicate the substantial promise of video models for advancing high-quality text-to-image generation.

