---
layout: default
title: The World is Your Canvas: Painting Promptable Events with Reference Images, Trajectories, and Text
---

# The World is Your Canvas: Painting Promptable Events with Reference Images, Trajectories, and Text
**arXiv**：[2512.16924v1](https://arxiv.org/abs/2512.16924) · [PDF](https://arxiv.org/pdf/2512.16924.pdf)  
**作者**：Hanlin Wang, Hao Ouyang, Qiuyu Wang, Yue Yu, Yihao Meng, Wen Wang, Ka Leong Cheng, Shuailei Ma, Qingyan Bai, Yixuan Li, Cheng Chen, Yanhong Zeng, Xing Zhu, Yujun Shen, Qifeng Chen  

**一句话要点**：提出WorldCanvas框架，通过结合文本、轨迹和参考图像实现用户可提示的世界事件生成。

**关键词**：世界事件生成, 多模态提示, 轨迹控制, 参考图像引导, 视频生成, 交互式模拟

## 3 点简述
- 核心问题：现有方法如纯文本或轨迹控制图像到视频生成在模拟复杂世界事件时存在局限性，难以实现多模态交互和对象一致性。
- 方法要点：采用多模态方法，结合轨迹编码运动、时间和可见性，自然语言表达语义意图，参考图像提供视觉基础，以生成可控事件。
- 实验或效果：生成视频展示时间连贯性和涌现一致性，支持多智能体交互、对象进出、参考引导外观和反直觉事件，提升世界模型交互性。

## 摘要（原文）

> We present WorldCanvas, a framework for promptable world events that enables rich, user-directed simulation by combining text, trajectories, and reference images. Unlike text-only approaches and existing trajectory-controlled image-to-video methods, our multimodal approach combines trajectories -- encoding motion, timing, and visibility -- with natural language for semantic intent and reference images for visual grounding of object identity, enabling the generation of coherent, controllable events that include multi-agent interactions, object entry/exit, reference-guided appearance and counterintuitive events. The resulting videos demonstrate not only temporal coherence but also emergent consistency, preserving object identity and scene despite temporary disappearance. By supporting expressive world events generation, WorldCanvas advances world models from passive predictors to interactive, user-shaped simulators. Our project page is available at: https://worldcanvas.github.io/.

