---
layout: default
title: STEC: A Reference-Free Spatio-Temporal Entropy Coverage Metric for Evaluating Sampled Video Frames
---

# STEC: A Reference-Free Spatio-Temporal Entropy Coverage Metric for Evaluating Sampled Video Frames
**arXiv**：[2601.13974v1](https://arxiv.org/abs/2601.13974) · [PDF](https://arxiv.org/pdf/2601.13974.pdf)  
**作者**：Shih-Yao Lin  

**一句话要点**：提出STEC无参考时空熵覆盖度量，以评估视频帧采样的信息覆盖质量

**关键词**：视频帧采样, 无参考评估, 时空熵, 信息覆盖, 视频理解

## 3 点简述
- 核心问题：现有指标不评估采样帧是否充分捕捉视频信息内容
- 方法要点：基于时空帧熵建模空间信息强度、时间分散性和非冗余性
- 实验或效果：在MSR-VTT基准上区分不同采样策略，揭示个体视频稳健性模式

## 摘要（原文）

> Frame sampling is a fundamental component in video understanding and video--language model pipelines, yet evaluating the quality of sampled frames remains challenging. Existing evaluation metrics primarily focus on perceptual quality or reconstruction fidelity, and are not designed to assess whether a set of sampled frames adequately captures informative and representative video content.
>   We propose Spatio-Temporal Entropy Coverage (STEC), a simple and non-reference metric for evaluating the effectiveness of video frame sampling. STEC builds upon Spatio-Temporal Frame Entropy (STFE), which measures per-frame spatial information via entropy-based structural complexity, and evaluates sampled frames based on their temporal coverage and redundancy. By jointly modeling spatial information strength, temporal dispersion, and non-redundancy, STEC provides a principled and lightweight measure of sampling quality.
>   Experiments on the MSR-VTT test-1k benchmark demonstrate that STEC clearly differentiates common sampling strategies, including random, uniform, and content-aware methods. We further show that STEC reveals robustness patterns across individual videos that are not captured by average performance alone, highlighting its practical value as a general-purpose evaluation tool for efficient video understanding.
>   We emphasize that STEC is not designed to predict downstream task accuracy, but to provide a task-agnostic diagnostic signal for analyzing frame sampling behavior under constrained budgets.

