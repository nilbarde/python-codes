# Comprehensive FFmpeg Commands Guide

This guide covers a variety of FFmpeg commands for common multimedia tasks on Ubuntu.

## Table of Contents

1. [Installing FFmpeg](#1-installing-ffmpeg)
2. [Converting Video Formats](#2-converting-video-formats)
3. [Trimming or Cutting Video](#3-trimming-or-cutting-video)
4. [Resizing Video](#4-resizing-video)
5. [Create Video using Images](#5-create-video-using-images)
6. [Record Video using URL](#6-record-video-using-url)
7. [Reducing Video Quality](#7-reducing-video-quality)
8. [Extract Images using Video](#8-extract-images-using-video)
9. [Overlay Video on Black Screen](#9-overlay-video-on-black-screen)

## 1. Installing FFmpeg

Install FFmpeg on Ubuntu:

```bash
sudo apt update
sudo apt install ffmpeg
```

## 2. Converting Video Formats

Convert a video file to another format:

```bash
ffmpeg -i input.mp4 output.avi
```

## 3. Trimming or Cutting Video

Trim or cut a specific portion from a video:

```bash
ffmpeg -i input.mp4 -ss 00:01:00 -to 00:02:30 -c copy output.mp4
```

## 4. Resizing Video

Resize a video to a specific resolution:

```bash
ffmpeg -i input.mp4 -vf scale=640:480 output.mp4
```

## 5. Create Video using Images

Create a video from a sequence of images:

```bash
ffmpeg -framerate 24 -pattern_type glob -i 'images/*.png' -c:v libx264 -pix_fmt yuv420p output.mp4
```

## 6. Record Video using URL

Record a video stream from a URL:

```bash
ffmpeg -i http://example.com/stream.m3u8 -c copy output.mp4
ffmpeg -i http://example.com/stream.m3u8 -rtsp_transport tcp -c copy -t 60 output.mp4
```

## 7. Reducing Video Quality

Reduce video quality by setting a specific bitrate:

```bash
ffmpeg -i input.mp4 -b:v 1M output.mp4
ffmpeg -i input.mp4 -vf "scale=480:480" -vcodec libx264 -crf 30 output.mp4
```

## 8. Extract Images using Video

Extract images at a specific interval from a video:

```bash
ffmpeg -i input.mp4 image-%05d.jpg
ffmpeg -i input.mp4 -vf fps=1/5 image-%03d.jpg
```

## 9. Overlay Video on Black Screen

Overlay a video on a black screen:

```bash
ffmpeg -i input.mp4 -vf "pad=width=1280:height=720:x=0:y=360" output.mp4
```
