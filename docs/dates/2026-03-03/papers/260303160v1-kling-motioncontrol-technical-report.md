---
layout: default
title: Kling-MotionControl Technical Report
---

# Kling-MotionControl Technical Report
**arXiv**：[2603.03160v1](https://arxiv.org/abs/2603.03160) · [PDF](https://arxiv.org/pdf/2603.03160.pdf)  
**作者**：Kling Team, Jialu Chen, Yikang Ding, Zhixue Fang, Kun Gai, Kang He, Xu He, Jingyun Hua, Mingming Lao, Xiaohan Li, Hui Liu, Jiwen Liu, Xiaoqiang Liu, Fan Shi, Xiaoyu Shi, Peiqin Sun, Songlin Tang, Pengfei Wan, Tiancheng Wen, Zhiyong Wu, Haoxian Zhang, Runze Zhao, Yuanxing Zhang, Yan Zhou  

**一句话要点**：提出Kling-MotionControl，基于DiT的统一框架，用于鲁棒、精确和表达丰富的整体角色动画生成。

**关键词**：角色动画, 扩散变换器, 运动控制, 身份无关学习, 多阶段蒸馏, 整体动画生成

## 3 点简述
- 核心问题：角色动画需从驱动视频迁移运动动态到参考图像，实现高保真和可控生成。
- 方法要点：采用分而治之策略，协调身体、面部和手部的异构运动表示，结合自适应身份无关学习和身份注入设计。
- 实验或效果：通过多阶段蒸馏加速推理速度超10倍，人类偏好评估显示在运动控制、泛化能力和视觉质量上优于领先方案。

## 摘要（原文）

> Character animation aims to generate lifelike videos by transferring motion dynamics from a driving video to a reference image. Recent strides in generative models have paved the way for high-fidelity character animation. In this work, we present Kling-MotionControl, a unified DiT-based framework engineered specifically for robust, precise, and expressive holistic character animation. Leveraging a divide-and-conquer strategy within a cohesive system, the model orchestrates heterogeneous motion representations tailored to the distinct characteristics of body, face, and hands, effectively reconciling large-scale structural stability with fine-grained articulatory expressiveness. To ensure robust cross-identity generalization, we incorporate adaptive identity-agnostic learning, facilitating natural motion retargeting for diverse characters ranging from realistic humans to stylized cartoons. Simultaneously, we guarantee faithful appearance preservation through meticulous identity injection and fusion designs, further supported by a subject library mechanism that leverages comprehensive reference contexts. To ensure practical utility, we implement an advanced acceleration framework utilizing multi-stage distillation, boosting inference speed by over 10x. Kling-MotionControl distinguishes itself through intelligent semantic motion understanding and precise text responsiveness, allowing for flexible control beyond visual inputs. Human preference evaluations demonstrate that Kling-MotionControl delivers superior performance compared to leading commercial and open-source solutions, achieving exceptional fidelity in holistic motion control, open domain generalization, and visual quality and coherence. These results establish Kling-MotionControl as a robust solution for high-quality, controllable, and lifelike character animation.

