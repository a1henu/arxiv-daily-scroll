---
layout: default
title: Tutti: Expressive Multi-Singer Synthesis via Structure-Level Timbre Control and Vocal Texture Modeling
---

# Tutti: Expressive Multi-Singer Synthesis via Structure-Level Timbre Control and Vocal Texture Modeling
**arXiv**：[2602.08233v1](https://arxiv.org/abs/2602.08233) · [PDF](https://arxiv.org/pdf/2602.08233.pdf)  
**作者**：Jiatao Chen, Xing Tang, Xiaoyue Duan, Yutang Feng, Jinchao Zhang, Jie Zhou  

**一句话要点**：提出Tutti框架，通过结构级音色控制和声纹建模解决多歌手合成中的动态安排与声学真实性问题。

**关键词**：多歌手合成, 音色控制, 声纹建模, 结构感知, 条件变分自编码器, 合唱生成

## 3 点简述
- 现有歌唱合成系统受限于全局音色控制，难以处理单曲内的动态多歌手安排和声学纹理。
- 引入结构感知歌手提示实现灵活歌手调度，并通过条件引导VAE进行互补纹理学习捕获隐式声学特征。
- 实验显示Tutti在多歌手调度和合唱生成的声学真实感方面表现优异，提供复杂多歌手安排的新范式。

## 摘要（原文）

> While existing Singing Voice Synthesis systems achieve high-fidelity solo performances, they are constrained by global timbre control, failing to address dynamic multi-singer arrangement and vocal texture within a single song. To address this, we propose Tutti, a unified framework designed for structured multi-singer generation. Specifically, we introduce a Structure-Aware Singer Prompt to enable flexible singer scheduling evolving with musical structure, and propose Complementary Texture Learning via Condition-Guided VAE to capture implicit acoustic textures (e.g., spatial reverberation and spectral fusion) that are complementary to explicit controls. Experiments demonstrate that Tutti excels in precise multi-singer scheduling and significantly enhances the acoustic realism of choral generation, offering a novel paradigm for complex multi-singer arrangement. Audio samples are available at https://annoauth123-ctrl.github.io/Tutii_Demo/.

