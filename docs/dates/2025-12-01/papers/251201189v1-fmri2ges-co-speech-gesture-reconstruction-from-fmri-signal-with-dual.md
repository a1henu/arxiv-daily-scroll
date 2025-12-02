---
layout: default
title: fMRI2GES: Co-speech Gesture Reconstruction from fMRI Signal with Dual Brain Decoding Alignment
---

# fMRI2GES: Co-speech Gesture Reconstruction from fMRI Signal with Dual Brain Decoding Alignment
**arXiv**：[2512.01189v1](https://arxiv.org/abs/2512.01189) · [PDF](https://arxiv.org/pdf/2512.01189.pdf)  
**作者**：Chunzheng Zhu, Jialin Shao, Jianxin Lin, Yijun Wang, Jing Wang, Jinhui Tang, Kenli Li  

**一句话要点**：提出fMRI2GES方法，通过双脑解码对齐从fMRI信号重建伴随语音的手势

**关键词**：脑信号解码, 手势重建, 多模态对齐, 自监督学习, fMRI分析

## 3 点简述
- 核心问题：缺乏配对脑-语音-手势数据，阻碍深度学习模型训练
- 方法要点：利用fMRI-文本和文本-手势模型，通过双模式对齐实现自监督训练
- 实验或效果：直接从fMRI记录重建表达性手势，分析不同脑区信号影响

## 摘要（原文）

> Understanding how the brain responds to external stimuli and decoding this process has been a significant challenge in neuroscience. While previous studies typically concentrated on brain-to-image and brain-to-language reconstruction, our work strives to reconstruct gestures associated with speech stimuli perceived by brain. Unfortunately, the lack of paired \{brain, speech, gesture\} data hinders the deployment of deep learning models for this purpose. In this paper, we introduce a novel approach, \textbf{fMRI2GES}, that allows training of fMRI-to-gesture reconstruction networks on unpaired data using \textbf{Dual Brain Decoding Alignment}. This method relies on two key components: (i) observed texts that elicit brain responses, and (ii) textual descriptions associated with the gestures. Then, instead of training models in a completely supervised manner to find a mapping relationship among the three modalities, we harness an fMRI-to-text model, a text-to-gesture model with paired data and an fMRI-to-gesture model with unpaired data, establishing dual fMRI-to-gesture reconstruction patterns. Afterward, we explicitly align two outputs and train our model in a self-supervision way. We show that our proposed method can reconstruct expressive gestures directly from fMRI recordings. We also investigate fMRI signals from different ROIs in the cortex and how they affect generation results. Overall, we provide new insights into decoding co-speech gestures, thereby advancing our understanding of neuroscience and cognitive science.

