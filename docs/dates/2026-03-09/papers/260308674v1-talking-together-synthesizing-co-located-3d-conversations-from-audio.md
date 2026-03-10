---
layout: default
title: Talking Together: Synthesizing Co-Located 3D Conversations from Audio
---

# Talking Together: Synthesizing Co-Located 3D Conversations from Audio
**arXiv**：[2603.08674v1](https://arxiv.org/abs/2603.08674) · [PDF](https://arxiv.org/pdf/2603.08674.pdf)  
**作者**：Mengyi Shan, Shouchieh Chang, Ziqian Bai, Shichen Liu, Yinda Zhang, Luchuan Song, Rohit Pandey, Sean Fanello, Zeng Huang  

**一句话要点**：提出双流架构以从混合音频合成共处3D对话动画，实现空间关系建模与控制。

**关键词**：3D面部动画, 音频驱动合成, 共处对话建模, 双流架构, 眼动控制, VR应用

## 3 点简述
- 核心问题：从混合音频生成共处两人的完整3D面部动画，包括空间关系和交互。
- 方法要点：使用双流架构、说话者角色嵌入和跨注意力机制，引入眼动损失和文本控制。
- 实验或效果：构建大规模数据集，生成流畅可控动画，在真实感和交互一致性上优于基线。

## 摘要（原文）

> We tackle the challenging task of generating complete 3D facial animations for two interacting, co-located participants from a mixed audio stream. While existing methods often produce disembodied "talking heads" akin to a video conference call, our work is the first to explicitly model the dynamic 3D spatial relationship -- including relative position, orientation, and mutual gaze -- that is crucial for realistic in-person dialogues. Our system synthesizes the full performance of both individuals, including precise lip-sync, and uniquely allows their relative head poses to be controlled via textual descriptions. To achieve this, we propose a dual-stream architecture where each stream is responsible for one participant's output. We employ speaker's role embeddings and inter-speaker cross-attention mechanisms designed to disentangle the mixed audio and model the interaction. Furthermore, we introduce a novel eye gaze loss to promote natural, mutual eye contact. To power our data-hungry approach, we introduce a novel pipeline to curate a large-scale conversational dataset consisting of over 2 million dyadic pairs from in-the-wild videos. Our method generates fluid, controllable, and spatially aware dyadic animations suitable for immersive applications in VR and telepresence, significantly outperforming existing baselines in perceived realism and interaction coherence.

