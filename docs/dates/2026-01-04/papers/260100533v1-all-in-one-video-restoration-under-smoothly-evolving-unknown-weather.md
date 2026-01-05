---
layout: default
title: All-in-One Video Restoration under Smoothly Evolving Unknown Weather Degradations
---

# All-in-One Video Restoration under Smoothly Evolving Unknown Weather Degradations
**arXiv**：[2601.00533v1](https://arxiv.org/abs/2601.00533) · [PDF](https://arxiv.org/pdf/2601.00533.pdf)  
**作者**：Wenrui Li, Hongtao Chen, Yao Xiao, Wangmeng Zuo, Jiantao Zhou, Yonghong Tian, Xiaopeng Fan  

**一句话要点**：提出ORCANet以解决视频修复中平滑演化未知天气退化的挑战

**关键词**：视频修复, 未知退化, 时间连续性, 提示生成, 自适应网络

## 3 点简述
- 核心问题：视频修复需处理随时间平滑演化的未知退化类型和强度，现有方法忽视时间连续性。
- 方法要点：设计CIED模块估计雾霾强度，FPG模块生成静态和动态提示以捕获退化特征。
- 实验或效果：ORCANet在恢复质量、时间一致性和鲁棒性上优于基线，代码已开源。

## 摘要（原文）

> All-in-one image restoration aims to recover clean images from diverse unknown degradations using a single model. But extending this task to videos faces unique challenges. Existing approaches primarily focus on frame-wise degradation variation, overlooking the temporal continuity that naturally exists in real-world degradation processes. In practice, degradation types and intensities evolve smoothly over time, and multiple degradations may coexist or transition gradually. In this paper, we introduce the Smoothly Evolving Unknown Degradations (SEUD) scenario, where both the active degradation set and degradation intensity change continuously over time. To support this scenario, we design a flexible synthesis pipeline that generates temporally coherent videos with single, compound, and evolving degradations. To address the challenges in the SEUD scenario, we propose an all-in-One Recurrent Conditional and Adaptive prompting Network (ORCANet). First, a Coarse Intensity Estimation Dehazing (CIED) module estimates haze intensity using physical priors and provides coarse dehazed features as initialization. Second, a Flow Prompt Generation (FPG) module extracts degradation features. FPG generates both static prompts that capture segment-level degradation types and dynamic prompts that adapt to frame-level intensity variations. Furthermore, a label-aware supervision mechanism improves the discriminability of static prompt representations under different degradations. Extensive experiments show that ORCANet achieves superior restoration quality, temporal consistency, and robustness over image and video-based baselines. Code is available at https://github.com/Friskknight/ORCANet-SEUD.

