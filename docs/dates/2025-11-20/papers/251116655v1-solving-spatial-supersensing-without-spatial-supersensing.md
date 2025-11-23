---
layout: default
title: Solving Spatial Supersensing Without Spatial Supersensing
---

# Solving Spatial Supersensing Without Spatial Supersensing
**arXiv**：[2511.16655v1](https://arxiv.org/abs/2511.16655) · [PDF](https://arxiv.org/pdf/2511.16655.pdf)  
**作者**：Vishaal Udandarao, Shyamgopal Karthik, Surabhi S. Nath, Andreas Hochlehnert, Matthias Bethge, Ameya Prabhu  

**一句话要点**：分析Cambrian-S基准与推理方法，揭示其未可靠测量空间超感知

**关键词**：空间超感知, 视频基准评估, 推理方法分析, 捷径启发式, 长视频理解

## 3 点简述
- 核心问题：当前VSI-Super基准可能无法有效评估空间超感知能力
- 方法要点：提出NoSense基线，仅用词袋模型解决VSR；设计VSC-Repeat扰动测试
- 实验或效果：NoSense在VSR达95%准确率；VSC-Repeat使Cambrian-S准确率降至0%

## 摘要（原文）

> Cambrian-S aims to take the first steps towards improving video world models with spatial supersensing by introducing (i) two benchmarks, VSI-Super-Recall (VSR) and VSI-Super-Counting (VSC), and (ii) bespoke predictive sensing inference strategies tailored to each benchmark. In this work, we conduct a critical analysis of Cambrian-S across both these fronts. First, we introduce a simple baseline, NoSense, which discards almost all temporal structure and uses only a bag-of-words SigLIP model, yet near-perfectly solves VSR, achieving 95% accuracy even on 4-hour videos. This shows benchmarks like VSR can be nearly solved without spatial cognition, world modeling or spatial supersensing. Second, we hypothesize that the tailored inference methods proposed by Cambrian-S likely exploit shortcut heuristics in the benchmark. We illustrate this with a simple sanity check on the VSC benchmark, called VSC-Repeat: We concatenate each video with itself 1-5 times, which does not change the number of unique objects. However, this simple perturbation entirely collapses the mean relative accuracy of Cambrian-S from 42% to 0%. A system that performs spatial supersensing and integrates information across experiences should recognize views of the same scene and keep object-count predictions unchanged; instead, Cambrian-S inference algorithm relies largely on a shortcut in the VSC benchmark that rooms are never revisited. Taken together, our findings suggest that (i) current VSI-Super benchmarks do not yet reliably measure spatial supersensing, and (ii) predictive-sensing inference recipes used by Cambrian-S improve performance by inadvertently exploiting shortcuts rather than from robust spatial supersensing. We include the response from the Cambrian-S authors (in Appendix A) to provide a balanced perspective alongside our claims. We release our code at: https://github.com/bethgelab/supersanity

