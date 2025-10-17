---
layout: default
title: From Language to Locomotion: Retargeting-free Humanoid Control via Motion Latent Guidance
---

# From Language to Locomotion: Retargeting-free Humanoid Control via Motion Latent Guidance
**arXiv**：[2510.14952v1](https://arxiv.org/abs/2510.14952) · [PDF](https://arxiv.org/pdf/2510.14952.pdf)  
**作者**：Zhe Li, Cheng Chi, Yangyang Wei, Boan Zhu, Yibo Peng, Tao Huang, Pengwei Wang, Zhongyuan Wang, Shanghang Zhang, Chang Xu  

**一句话要点**：提出RoboGhost框架，通过运动潜在引导实现免重定向的人形机器人控制

**关键词**：人形机器人控制, 语言到动作, 扩散策略, 运动潜在表示, 免重定向框架

## 3 点简述
- 现有语言引导人形机器人运动流程繁琐，易累积误差且语义与控制耦合弱
- RoboGhost直接基于语言接地运动潜在，使用扩散策略从噪声去噪生成可执行动作
- 实验显示RoboGhost降低延迟、提高成功率与跟踪精度，支持多模态扩展

## 摘要（原文）

> Natural language offers a natural interface for humanoid robots, but existing
> language-guided humanoid locomotion pipelines remain cumbersome and unreliable.
> They typically decode human motion, retarget it to robot morphology, and then
> track it with a physics-based controller. However, this multi-stage process is
> prone to cumulative errors, introduces high latency, and yields weak coupling
> between semantics and control. These limitations call for a more direct pathway
> from language to action, one that eliminates fragile intermediate stages.
> Therefore, we present RoboGhost, a retargeting-free framework that directly
> conditions humanoid policies on language-grounded motion latents. By bypassing
> explicit motion decoding and retargeting, RoboGhost enables a diffusion-based
> policy to denoise executable actions directly from noise, preserving semantic
> intent and supporting fast, reactive control. A hybrid causal
> transformer-diffusion motion generator further ensures long-horizon consistency
> while maintaining stability and diversity, yielding rich latent representations
> for precise humanoid behavior. Extensive experiments demonstrate that RoboGhost
> substantially reduces deployment latency, improves success rates and tracking
> accuracy, and produces smooth, semantically aligned locomotion on real
> humanoids. Beyond text, the framework naturally extends to other modalities
> such as images, audio, and music, providing a general foundation for
> vision-language-action humanoid systems.

