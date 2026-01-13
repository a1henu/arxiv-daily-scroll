---
layout: default
title: Improving Video Question Answering through query-based frame selection
---

# Improving Video Question Answering through query-based frame selection
**arXiv**：[2601.07459v1](https://arxiv.org/abs/2601.07459) · [PDF](https://arxiv.org/pdf/2601.07459.pdf)  
**作者**：Himanshu Patil, Geo Jolly, Ramana Raja Buddala, Ganesh Ramakrishnan, Rohit Saluja  

**一句话要点**：提出基于查询的帧选择方法以提升视频问答准确性，通过子模互信息函数选取关键帧。

**关键词**：视频问答, 帧选择, 子模互信息, 视觉语言模型, 多动作视频任务

## 3 点简述
- 视频问答模型常因计算限制而均匀采样帧，忽略问题相关性和视频上下文。
- 采用基于查询的帧选择，利用子模互信息函数选取互补且必要的视觉信息。
- 在MVBench数据集上评估，使用Video-LLaVA和LLaVA-NeXT模型，准确率提升最高达4%。

## 摘要（原文）

> Video Question Answering (VideoQA) models enhance understanding and interaction with audiovisual content, making it more accessible, searchable, and useful for a wide range of fields such as education, surveillance, entertainment, and content creation. Due to heavy compute requirements, most large visual language models (VLMs) for VideoQA rely on a fixed number of frames by uniformly sampling the video. However, this process does not pick important frames or capture the context of the video. We present a novel query-based selection of frames relevant to the questions based on the submodular mutual Information (SMI) functions. By replacing uniform frame sampling with query-based selection, our method ensures that the chosen frames provide complementary and essential visual information for accurate VideoQA. We evaluate our approach on the MVBench dataset, which spans a diverse set of multi-action video tasks. VideoQA accuracy on this dataset was assessed using two VLMs, namely Video-LLaVA and LLaVA-NeXT, both of which originally employed uniform frame sampling. Experiments were conducted using both uniform and query-based sampling strategies. An accuracy improvement of up to \textbf{4\%} was observed when using query-based frame selection over uniform sampling. Qualitative analysis further highlights that query-based selection, using SMI functions, consistently picks frames better aligned with the question. We opine that such query-based frame selection can enhance accuracy in a wide range of tasks that rely on only a subset of video frames.

